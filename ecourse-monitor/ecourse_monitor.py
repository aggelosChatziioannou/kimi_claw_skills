#!/usr/bin/env python3
"""
Ecourse Monitor - Automatic UOI ecourse announcement tracking
"""

import json
import time
from datetime import datetime
from pathlib import Path

# Configuration
SKILL_DIR = Path("/root/.openclaw/skills/ecourse-monitor")
MEMORY_DIR = Path("/root/.openclaw/workspace/memory/ecourse")
DATA_FILE = MEMORY_DIR / "announcements.json"
COURSES_FILE = SKILL_DIR / "courses.json"

def ensure_directories():
    """Ensure all required directories exist."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def get_courses():
    """Get list of monitored courses."""
    return [
        {
            "name": "ΜΥΕ017 Κατανεμημένα Συστήματα",
            "course_id": 4384,
            "forum_id": 159378,
            "forum_url": "https://ecourse.uoi.gr/mod/forum/view.php?id=159378"
        },
        {
            "name": "Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας",
            "course_id": 2114,
            "forum_id": 159988,
            "forum_url": "https://ecourse.uoi.gr/mod/forum/view.php?id=159988"
        },
        {
            "name": "Διακριτά Μαθηματικά ΙI",
            "course_id": 3097,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "Διδακτική της Πληροφορικής",
            "course_id": 1916,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "Δίκτυα Υπολογιστών I (MYY703)",
            "course_id": 869,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "Εξόρυξη δεδομένων",
            "course_id": 1024,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "ΜΙΚΡΟΕΠΕΞΕΡΓΑΣΤΕΣ",
            "course_id": 1823,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "Προχωρημένα Θέματα Τεχνολογίας και Εφαρμογών Βάσεων",
            "course_id": 2194,
            "forum_id": None,
            "forum_url": None
        },
        {
            "name": "Υπολογιστική Όραση",
            "course_id": 1678,
            "forum_id": None,
            "forum_url": None
        }
    ]

def load_data():
    """Load stored announcement data."""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "last_check": None,
        "courses": {},
        "all_announcements": []
    }

def save_data(data):
    """Save announcement data."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)

def check_course(browser, course):
    """Check a single course for announcements."""
    print(f"\n📚 Checking: {course['name']}")
    
    if not course.get('forum_url'):
        print(f"   ⚠️ No forum URL configured yet")
        return []
    
    try:
        # Navigate to course forum
        browser.navigate(course['forum_url'])
        time.sleep(2)
        
        # Extract announcements from page
        # This would use browser.snapshot() in real implementation
        # For now, return empty list
        announcements = []
        
        print(f"   ✅ Found {len(announcements)} announcements")
        return announcements
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return []

def compare_announcements(old_list, new_list):
    """Find new announcements by comparing lists."""
    old_ids = {a.get('id') for a in old_list if a.get('id')}
    new_announcements = []
    
    for announcement in new_list:
        if announcement.get('id') and announcement['id'] not in old_ids:
            new_announcements.append(announcement)
    
    return new_announcements

def format_notification(new_announcements):
    """Format Telegram notification."""
    if not new_announcements:
        return None
    
    lines = [
        "📚 **ΝΕΕΣ ΑΝΑΚΟΙΝΩΣΕΙΣ ECOURSE**",
        "",
        f"🔔 Βρέθηκαν {len(new_announcements)} νέες ανακοινώσεις:",
        ""
    ]
    
    for ann in new_announcements:
        lines.append(f"**{ann['course_name']}**")
        lines.append(f"📌 {ann['title']}")
        lines.append(f"👤 {ann['author']}")
        lines.append(f"📅 {ann['date']}")
        lines.append("")
    
    return "\n".join(lines)

def run_check(browser=None):
    """Run full ecourse check."""
    print("=" * 60)
    print("📚 ECOURSE MONITOR - STARTING CHECK")
    print("=" * 60)
    print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    ensure_directories()
    data = load_data()
    courses = get_courses()
    
    all_new_announcements = []
    
    for course in courses:
        # Check each course
        announcements = check_course(browser, course)
        
        # Get previous announcements for this course
        course_id = str(course['course_id'])
        old_announcements = data['courses'].get(course_id, [])
        
        # Find new announcements
        new_announcements = compare_announcements(old_announcements, announcements)
        
        if new_announcements:
            for ann in new_announcements:
                ann['course_name'] = course['name']
                ann['course_id'] = course['course_id']
            all_new_announcements.extend(new_announcements)
        
        # Update stored data
        data['courses'][course_id] = announcements
    
    # Update last check time
    data['last_check'] = datetime.now().isoformat()
    
    # Save data
    save_data(data)
    
    # Generate notification if new announcements found
    notification = None
    if all_new_announcements:
        notification = format_notification(all_new_announcements)
        print("\n" + "=" * 60)
        print("🔔 NEW ANNOUNCEMENTS FOUND!")
        print("=" * 60)
        print(notification)
    else:
        print("\n" + "=" * 60)
        print("✅ No new announcements")
        print("=" * 60)
    
    return {
        "new_announcements": all_new_announcements,
        "notification": notification,
        "total_courses": len(courses),
        "last_check": data['last_check']
    }

def get_summary():
    """Get summary of all announcements for morning briefing."""
    data = load_data()
    courses = get_courses()
    
    total_announcements = 0
    course_summaries = []
    
    for course in courses:
        course_id = str(course['course_id'])
        course_data = data['courses'].get(course_id, {})
        
        # Handle different data structures
        if isinstance(course_data, dict):
            announcements = course_data.get('announcements', [])
        elif isinstance(course_data, list):
            announcements = course_data
        else:
            announcements = []
        
        total_announcements += len(announcements)
        
        if announcements:
            # Get most recent
            try:
                recent = sorted(announcements, key=lambda x: x.get('date', '') if isinstance(x, dict) else '', reverse=True)[:2]
            except:
                recent = announcements[:2] if announcements else []
            
            course_summaries.append({
                "name": course['name'],
                "count": len(announcements),
                "recent": recent
            })
    
    return {
        "total_courses": len(courses),
        "total_announcements": total_announcements,
        "last_check": data.get('last_check'),
        "course_summaries": course_summaries
    }

def format_morning_briefing():
    """Format morning briefing text."""
    summary = get_summary()
    
    lines = [
        "📚 **ECOURSE CHECK**",
        ""
    ]
    
    if summary['course_summaries']:
        lines.append(f"📊 Σύνολο: {summary['total_announcements']} ανακοινώσεις σε {len(summary['course_summaries'])} μαθήματα")
        lines.append("")
        
        for cs in summary['course_summaries'][:5]:  # Show top 5
            lines.append(f"**{cs['name']}** ({cs['count']} ανακοινώσεις)")
            for ann in cs['recent'][:1]:  # Show most recent
                lines.append(f"  • {ann.get('title', 'N/A')}")
            lines.append("")
    else:
        lines.append("📭 Καμία ανακοίνωση ακόμα")
    
    lines.append(f"⏱️ Τελευταίος έλεγχος: {summary['last_check'][:16] if summary['last_check'] else 'Ποτέ'}")
    
    return "\n".join(lines)

if __name__ == "__main__":
    # Test mode
    print("Testing Ecourse Monitor...")
    result = run_check()
    print("\nMorning Briefing Format:")
    print(format_morning_briefing())
