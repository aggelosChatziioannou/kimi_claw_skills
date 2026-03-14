#!/usr/bin/env python3
"""
Cron Monitor - Automatic cron job health monitoring
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
SKILL_DIR = Path("/root/.openclaw/skills/cron-monitor")
MEMORY_DIR = Path("/root/.openclaw/workspace/memory/cron-monitor")
DATA_FILE = MEMORY_DIR / "monitoring.json"

# Thresholds
WARN_CONSECUTIVE_ERRORS = 2
CRITICAL_CONSECUTIVE_ERRORS = 3
WARN_DURATION_MINUTES = 5
CRITICAL_DURATION_MINUTES = 10
WARN_SUCCESS_RATE = 0.8
CRITICAL_SUCCESS_RATE = 0.5

# Known error patterns
ERROR_PATTERNS = {
    "rate_limit": ["rate limit", "too many requests", "429"],
    "timeout": ["timeout", "timed out", "deadline exceeded"],
    "gateway": ["gateway", "connection refused", "ECONNREFUSED"],
    "auth": ["unauthorized", "authentication failed", "401", "403"],
}

def ensure_directories():
    """Ensure all required directories exist."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    """Load monitoring data."""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "last_check": None,
        "alerts_sent": [],
        "job_stats": {}
    }

def save_data(data):
    """Save monitoring data."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)

def classify_error(error_text):
    """Classify error type from error text."""
    error_lower = error_text.lower()
    for error_type, patterns in ERROR_PATTERNS.items():
        for pattern in patterns:
            if pattern in error_lower:
                return error_type
    return "unknown"

def get_severity(job, last_run):
    """Determine severity level for a job."""
    issues = []
    severity = "ok"  # ok, warning, critical
    
    if not last_run:
        return "warning", ["No run history available"]
    
    # Check consecutive errors
    consecutive_errors = last_run.get('consecutiveErrors', 0)
    if consecutive_errors >= CRITICAL_CONSECUTIVE_ERRORS:
        severity = "critical"
        issues.append(f"Failed {consecutive_errors} times in a row")
    elif consecutive_errors >= WARN_CONSECUTIVE_ERRORS:
        severity = max(severity, "warning")
        issues.append(f"Failed {consecutive_errors} consecutive times")
    
    # Check duration
    duration_ms = last_run.get('durationMs', 0)
    duration_min = duration_ms / 60000
    if duration_min > CRITICAL_DURATION_MINUTES:
        severity = "critical"
        issues.append(f"Last run took {duration_min:.1f} min (very slow)")
    elif duration_min > WARN_DURATION_MINUTES:
        severity = max(severity, "warning")
        issues.append(f"Last run took {duration_min:.1f} min (slow)")
    
    # Check last status
    last_status = last_run.get('lastStatus')
    if last_status == "error":
        error_text = last_run.get('lastError', '')
        error_type = classify_error(error_text)
        
        if error_type in ['rate_limit', 'gateway']:
            severity = max(severity, "warning")
            issues.append(f"Transient error: {error_type}")
        else:
            severity = max(severity, "warning")
            issues.append(f"Last run failed: {error_type}")
    
    return severity, issues

def format_alert(job_name, severity, issues, job_info):
    """Format alert message."""
    icons = {
        "ok": "✅",
        "warning": "⚠️",
        "critical": "🚨"
    }
    
    headers = {
        "ok": "**CRON JOB OK**",
        "warning": "**CRON JOB WARNING**",
        "critical": "**CRON JOB CRITICAL**"
    }
    
    lines = [
        f"{icons.get(severity, '⚠️')} {headers.get(severity, '**CRON ALERT**')}",
        "",
        f"📋 **Job:** {job_name}",
    ]
    
    if issues:
        lines.append(f"⚠️ **Issues:**")
        for issue in issues:
            lines.append(f"  • {issue}")
    
    # Add last run info
    last_run = job_info.get('state', {})
    if last_run.get('lastRunAtMs'):
        last_run_time = datetime.fromtimestamp(last_run['lastRunAtMs'] / 1000).strftime('%Y-%m-%d %H:%M')
        lines.append(f"\n⏱️ **Last Run:** {last_run_time}")
    
    if last_run.get('lastDurationMs'):
        duration_min = last_run['lastDurationMs'] / 60000
        lines.append(f"⏱️ **Duration:** {duration_min:.1f} min")
    
    # Suggest fix
    if severity == "critical":
        lines.append("\n🔧 **Suggested Action:** Check logs and restart Gateway if needed")
    elif severity == "warning":
        lines.append("\n💡 **Suggested Action:** Monitor for next run")
    
    return "\n".join(lines)

def format_summary(jobs_health):
    """Format daily summary."""
    total = len(jobs_health)
    ok_count = sum(1 for j in jobs_health if j['severity'] == 'ok')
    warning_count = sum(1 for j in jobs_health if j['severity'] == 'warning')
    critical_count = sum(1 for j in jobs_health if j['severity'] == 'critical')
    
    lines = [
        "📊 **CRON HEALTH SUMMARY**",
        "",
        f"📋 Total Jobs: {total}",
        f"✅ Healthy: {ok_count}",
    ]
    
    if warning_count > 0:
        lines.append(f"⚠️ Warnings: {warning_count}")
    if critical_count > 0:
        lines.append(f"🚨 Critical: {critical_count}")
    
    lines.append("")
    
    # Overall health
    if critical_count > 0:
        lines.append("🚨 **Overall: ACTION REQUIRED**")
    elif warning_count > 0:
        lines.append("⚠️ **Overall: NEEDS ATTENTION**")
    else:
        lines.append("✅ **Overall: ALL GOOD**")
    
    # List problematic jobs
    problem_jobs = [j for j in jobs_health if j['severity'] != 'ok']
    if problem_jobs:
        lines.append("\n📋 **Jobs Needing Attention:**")
        for job in problem_jobs:
            icon = "🚨" if job['severity'] == 'critical' else "⚠️"
            lines.append(f"{icon} {job['name']}")
    
    return "\n".join(lines)

def check_jobs(cron_list_result):
    """Check all cron jobs and return health status."""
    jobs = cron_list_result.get('jobs', [])
    jobs_health = []
    alerts = []
    
    for job in jobs:
        job_name = job.get('name', 'Unknown')
        state = job.get('state', {})
        
        severity, issues = get_severity(job, state)
        
        jobs_health.append({
            'id': job.get('id'),
            'name': job_name,
            'severity': severity,
            'issues': issues,
            'enabled': job.get('enabled', True)
        })
        
        # Generate alert for non-ok jobs
        if severity != 'ok':
            alert = format_alert(job_name, severity, issues, job)
            alerts.append({
                'job_id': job.get('id'),
                'job_name': job_name,
                'severity': severity,
                'message': alert
            })
    
    return jobs_health, alerts

def should_send_alert(job_id, severity, data):
    """Check if we should send alert (avoid spam)."""
    alerts_sent = data.get('alerts_sent', [])
    
    # Find last alert for this job
    last_alert = None
    for alert in reversed(alerts_sent):
        if alert.get('job_id') == job_id:
            last_alert = alert
            break
    
    if not last_alert:
        return True
    
    # Don't repeat same severity within 1 hour
    last_time = datetime.fromisoformat(last_alert.get('time', '2000-01-01'))
    if (datetime.now() - last_time) < timedelta(hours=1):
        if last_alert.get('severity') == severity:
            return False
    
    return True

def record_alert(job_id, severity, data):
    """Record that we sent an alert."""
    if 'alerts_sent' not in data:
        data['alerts_sent'] = []
    
    data['alerts_sent'].append({
        'job_id': job_id,
        'severity': severity,
        'time': datetime.now().isoformat()
    })
    
    # Keep only last 100 alerts
    data['alerts_sent'] = data['alerts_sent'][-100:]

def run_check(cron_list_result, send_alerts=True):
    """Run full cron health check."""
    ensure_directories()
    data = load_data()
    
    jobs_health, alerts = check_jobs(cron_list_result)
    
    # Update data
    data['last_check'] = datetime.now().isoformat()
    data['job_stats'] = {j['id']: {'severity': j['severity'], 'issues': j['issues']} for j in jobs_health}
    
    # Determine which alerts to send
    alerts_to_send = []
    for alert in alerts:
        if send_alerts and should_send_alert(alert['job_id'], alert['severity'], data):
            alerts_to_send.append(alert)
            record_alert(alert['job_id'], alert['severity'], data)
    
    save_data(data)
    
    # Generate summary
    summary = format_summary(jobs_health)
    
    return {
        'jobs_health': jobs_health,
        'alerts': alerts_to_send,
        'summary': summary,
        'total_jobs': len(jobs_health),
        'ok_jobs': sum(1 for j in jobs_health if j['severity'] == 'ok'),
        'warning_jobs': sum(1 for j in jobs_health if j['severity'] == 'warning'),
        'critical_jobs': sum(1 for j in jobs_health if j['severity'] == 'critical')
    }

def format_health_report(result):
    """Format complete health report."""
    lines = [
        result['summary'],
        "",
        "📊 **Statistics:**",
        f"  • Total Jobs: {result['total_jobs']}",
        f"  • Healthy: {result['ok_jobs']}",
        f"  • Warnings: {result['warning_jobs']}",
        f"  • Critical: {result['critical_jobs']}",
    ]
    
    if result['alerts']:
        lines.append("\n🚨 **Active Alerts:**")
        for alert in result['alerts']:
            lines.append(alert['message'])
            lines.append("")
    
    return "\n".join(lines)

if __name__ == "__main__":
    print("Cron Monitor - Run through OpenClaw with cron.list result")
