#!/usr/bin/env python3
"""
Sub-Agent Monitor - Track and announce sub-agent activity
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

# Configuration
MEMORY_FILE = Path("/root/.openclaw/workspace/memory/sub-agent-monitor.json")

# Category mappings with icons
CATEGORY_CONFIG = {
    "research": {"icon": "🔍", "priority": 3, "examples": ["research", "search", "investigate"]},
    "code": {"icon": "💻", "priority": 3, "examples": ["code", "review", "bug", "fix", "refactor"]},
    "analysis": {"icon": "📊", "priority": 2, "examples": ["analyze", "report", "summary", "data"]},
    "learning": {"icon": "🧠", "priority": 1, "examples": ["learn", "improve", "study", "train"]},
    "execution": {"icon": "⚙️", "priority": 2, "examples": ["execute", "run", "deploy", "task"]},
    "planning": {"icon": "📋", "priority": 2, "examples": ["plan", "organize", "schedule"]},
    "writing": {"icon": "✍️", "priority": 2, "examples": ["write", "draft", "compose", "edit"]},
}


class SubAgentMonitor:
    """Monitor and track sub-agent activity."""
    
    def __init__(self):
        self.active_agents: Dict[str, Dict] = {}
        self.completed_agents: List[Dict] = []
        self._load_state()
    
    def _load_state(self):
        """Load monitor state from memory."""
        if MEMORY_FILE.exists():
            try:
                with open(MEMORY_FILE, 'r') as f:
                    data = json.load(f)
                    self.active_agents = data.get("active", {})
                    self.completed_agents = data.get("completed", [])[-20:]  # Keep last 20
            except Exception:
                pass
    
    def _save_state(self):
        """Save monitor state to memory."""
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_FILE, 'w') as f:
            json.dump({
                "active": self.active_agents,
                "completed": self.completed_agents[-20:],  # Keep last 20
                "last_updated": datetime.now().isoformat()
            }, f, indent=2, default=str)
    
    def detect_category(self, task_description: str) -> tuple:
        """Detect category from task description."""
        task_lower = task_description.lower()
        
        for category, config in CATEGORY_CONFIG.items():
            for keyword in config["examples"]:
                if keyword in task_lower:
                    return category, config["icon"]
        
        return "execution", "⚙️"  # Default
    
    def estimate_duration(self, task_description: str) -> str:
        """Estimate task duration based on keywords."""
        task_lower = task_description.lower()
        
        if any(word in task_lower for word in ["quick", "simple", "check"]):
            return "2-5 minutes"
        elif any(word in task_lower for word in ["research", "deep", "comprehensive"]):
            return "10-20 minutes"
        elif any(word in task_lower for word in ["analysis", "review", "complex"]):
            return "5-15 minutes"
        else:
            return "5-10 minutes"
    
    def register_agent(self, agent_id: str, name: str, task: str, 
                       agent_type: str = "auto") -> Dict:
        """Register a new sub-agent when it starts."""
        category, icon = self.detect_category(task) if agent_type == "auto" else (agent_type, "⚙️")
        
        agent_info = {
            "id": agent_id,
            "name": name,
            "task": task,
            "category": category,
            "icon": icon,
            "start_time": datetime.now().isoformat(),
            "status": "running",
            "progress": 0,
            "progress_text": "Starting...",
            "estimated_duration": self.estimate_duration(task)
        }
        
        self.active_agents[agent_id] = agent_info
        self._save_state()
        
        return agent_info
    
    def update_progress(self, agent_id: str, progress: int, 
                       progress_text: Optional[str] = None):
        """Update sub-agent progress."""
        if agent_id in self.active_agents:
            self.active_agents[agent_id]["progress"] = min(progress, 100)
            if progress_text:
                self.active_agents[agent_id]["progress_text"] = progress_text
            self._save_state()
    
    def complete_agent(self, agent_id: str, result_summary: str = "") -> Optional[Dict]:
        """Mark sub-agent as completed."""
        if agent_id in self.active_agents:
            agent = self.active_agents.pop(agent_id)
            agent["end_time"] = datetime.now().isoformat()
            agent["status"] = "completed"
            agent["result_summary"] = result_summary
            
            # Calculate duration
            start = datetime.fromisoformat(agent["start_time"])
            end = datetime.fromisoformat(agent["end_time"])
            agent["duration_minutes"] = round((end - start).total_seconds() / 60, 1)
            
            self.completed_agents.append(agent)
            self._save_state()
            
            return agent
        return None
    
    def fail_agent(self, agent_id: str, error: str = "") -> Optional[Dict]:
        """Mark sub-agent as failed."""
        if agent_id in self.active_agents:
            agent = self.active_agents.pop(agent_id)
            agent["end_time"] = datetime.now().isoformat()
            agent["status"] = "failed"
            agent["error"] = error
            
            self.completed_agents.append(agent)
            self._save_state()
            
            return agent
        return None
    
    def get_elapsed_time(self, agent: Dict) -> str:
        """Get human-readable elapsed time."""
        start = datetime.fromisoformat(agent["start_time"])
        elapsed = datetime.now() - start
        
        minutes = int(elapsed.total_seconds() / 60)
        if minutes < 1:
            return "just now"
        elif minutes == 1:
            return "1 min"
        elif minutes < 60:
            return f"{minutes} min"
        else:
            hours = minutes // 60
            mins = minutes % 60
            return f"{hours}h {mins}m"
    
    def format_start_announcement(self, agent: Dict) -> str:
        """Format announcement when sub-agent starts."""
        icon = agent["icon"]
        name = agent["name"]
        task = agent["task"]
        duration = agent["estimated_duration"]
        
        return f"""🚀 **SUB-AGENT STARTED**

{icon} **{name}**
• Task: {task}
• Estimated: {duration}
• Status: Initializing..."""
    
    def format_status_footer(self, include_header: bool = True) -> str:
        """Format status footer for appending to messages."""
        if not self.active_agents:
            return ""
        
        lines = []
        if include_header:
            lines.append("\n---")
            count = len(self.active_agents)
            lines.append(f"⚙️ **ACTIVE SUB-AGENT{'S' if count > 1 else ''} ({count})**")
        
        # Sort by priority (high first)
        sorted_agents = sorted(
            self.active_agents.values(),
            key=lambda x: CATEGORY_CONFIG.get(x["category"], {}).get("priority", 0),
            reverse=True
        )
        
        for i, agent in enumerate(sorted_agents, 1):
            icon = agent["icon"]
            name = agent["name"]
            task = agent["task"][:40] + "..." if len(agent["task"]) > 40 else agent["task"]
            elapsed = self.get_elapsed_time(agent)
            progress = agent.get("progress", 0)
            progress_text = agent.get("progress_text", "")
            
            lines.append(f"\n{i}. {icon} **{name}** ({elapsed})")
            lines.append(f"   • Task: {task}")
            if progress > 0:
                lines.append(f"   • Progress: {progress}% - {progress_text}")
        
        if len(sorted_agents) > 0:
            lines.append("\n💡 *Working in background. I'll notify when complete.*")
        
        return "\n".join(lines)
    
    def format_completion_announcement(self, agent: Dict) -> str:
        """Format announcement when sub-agent completes."""
        icon = agent["icon"]
        name = agent["name"]
        duration = agent.get("duration_minutes", "?")
        result = agent.get("result_summary", "Task completed successfully")
        
        return f"""✅ **SUB-AGENT COMPLETED**

{icon} **{name}** finished!
• Duration: {duration} minutes
• Result: {result}
• Status: ✅ Success"""
    
    def format_failure_announcement(self, agent: Dict) -> str:
        """Format announcement when sub-agent fails."""
        icon = agent["icon"]
        name = agent["name"]
        error = agent.get("error", "Unknown error")
        
        return f"""❌ **SUB-AGENT FAILED**

{icon} **{name}** encountered an issue
• Error: {error}
• Status: ❌ Failed

💡 You can retry or check logs for details."""
    
    def has_active_agents(self) -> bool:
        """Check if any sub-agents are active."""
        return len(self.active_agents) > 0
    
    def get_active_count(self) -> int:
        """Get count of active sub-agents."""
        return len(self.active_agents)
    
    def cleanup_stale(self, max_age_minutes: int = 60):
        """Remove agents that seem stuck (optional cleanup)."""
        stale = []
        now = datetime.now()
        
        for agent_id, agent in self.active_agents.items():
            start = datetime.fromisoformat(agent["start_time"])
            if (now - start) > timedelta(minutes=max_age_minutes):
                stale.append(agent_id)
        
        for agent_id in stale:
            self.fail_agent(agent_id, "Timed out (stale)")
        
        return len(stale)


# Global instance
_monitor = None

def get_monitor() -> SubAgentMonitor:
    """Get or create global monitor instance."""
    global _monitor
    if _monitor is None:
        _monitor = SubAgentMonitor()
    return _monitor


# Convenience functions for direct use
def announce_start(agent_id: str, name: str, task: str) -> str:
    """Register and announce sub-agent start. Returns announcement text."""
    monitor = get_monitor()
    agent = monitor.register_agent(agent_id, name, task)
    return monitor.format_start_announcement(agent)

def announce_completion(agent_id: str, result: str = "") -> str:
    """Announce sub-agent completion. Returns announcement text."""
    monitor = get_monitor()
    agent = monitor.complete_agent(agent_id, result)
    if agent:
        return monitor.format_completion_announcement(agent)
    return ""

def get_status_footer() -> str:
    """Get status footer for appending to messages."""
    monitor = get_monitor()
    return monitor.format_status_footer()

def has_active() -> bool:
    """Check if any sub-agents are active."""
    monitor = get_monitor()
    return monitor.has_active_agents()


# Demo/test
if __name__ == "__main__":
    monitor = SubAgentMonitor()
    
    print("=" * 60)
    print("SUB-AGENT MONITOR DEMO")
    print("=" * 60)
    
    # Simulate spawning agents
    agent1 = monitor.register_agent("agent:001", "Deep Research", "Research AI trends for Q1 2026")
    print("\n" + monitor.format_start_announcement(agent1))
    print("\n" + "-" * 40)
    
    agent2 = monitor.register_agent("agent:002", "Code Review", "Review src/components for bugs")
    print("\n" + monitor.format_start_announcement(agent2))
    print("\n" + "-" * 40)
    
    # Simulate progress
    monitor.update_progress("agent:001", 45, "Analyzing sources...")
    monitor.update_progress("agent:002", 60, "3/5 files checked")
    
    # Show status footer
    print("\n" + monitor.format_status_footer())
    print("\n" + "=" * 60)
    
    # Complete one
    completed = monitor.complete_agent("agent:001", "Found 3 relevant trends")
    print("\n" + monitor.format_completion_announcement(completed))
    print("\n" + "=" * 60)
    
    # Show remaining
    print("\n" + monitor.format_status_footer())
