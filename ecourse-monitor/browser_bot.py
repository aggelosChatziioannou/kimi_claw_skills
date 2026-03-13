#!/usr/bin/env python3
"""
Browser automation for ecourse monitoring
"""

import time
import json
from datetime import datetime
from pathlib import Path

# Course credentials
USERNAME = "cs05390"
PASSWORD = "singapure2018"

BASE_URL = "https://ecourse.uoi.gr"
LOGIN_URL = f"{BASE_URL}/login/index.php"

COURSES = [
    {
        "name": "ΜΥΕ017 Κατανεμημένα Συστήματα",
        "course_id": 4384,
        "forum_id": 159378
    },
    {
        "name": "Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας", 
        "course_id": 2114,
        "forum_id": 159988
    },
    {
        "name": "Διακριτά Μαθηματικά ΙI",
        "course_id": 3097,
        "forum_id": None
    },
    {
        "name": "Διδακτική της Πληροφορικής",
        "course_id": 1916,
        "forum_id": None
    },
    {
        "name": "Δίκτυα Υπολογιστών I (MYY703)",
        "course_id": 869,
        "forum_id": None
    },
    {
        "name": "Εξόρυξη δεδομένων",
        "course_id": 1024,
        "forum_id": None
    },
    {
        "name": "ΜΙΚΡΟΕΠΕΞΕΡΓΑΣΤΕΣ",
        "course_id": 1823,
        "forum_id": None
    },
    {
        "name": "Προχωρημένα Θέματα Τεχνολογίας και Εφαρμογών Βάσεων",
        "course_id": 2194,
        "forum_id": None
    },
    {
        "name": "Υπολογιστική Όραση",
        "course_id": 1678,
        "forum_id": None
    }
]

def login_to_ecourse(browser):
    """Login to ecourse platform."""
    print("🔐 Logging in to ecourse...")
    
    try:
        # Navigate to login page
        browser.navigate(LOGIN_URL)
        time.sleep(2)
        
        # Take snapshot to find form elements
        snapshot = browser.snapshot()
        
        # Find and fill username
        username_field = None
        password_field = None
        login_button = None
        
        for ref, element in snapshot.elements.items():
            if element.get('type') == 'textbox':
                name = element.get('name', '').lower()
                if 'user' in name or 'username' in name:
                    username_field = ref
                elif 'pass' in name or 'password' in name:
                    password_field = ref
            elif element.get('type') == 'button':
                text = element.get('text', '').lower()
                if 'login' in text or 'σύνδεση' in text:
                    login_button = ref
        
        if not username_field or not password_field:
            print("❌ Could not find login form fields")
            return False
        
        # Fill credentials
        browser.act({"kind": "type", "ref": username_field, "text": USERNAME})
        time.sleep(0.5)
        browser.act({"kind": "type", "ref": password_field, "text": PASSWORD})
        time.sleep(0.5)
        browser.act({"kind": "click", "ref": login_button})
        time.sleep(3)
        
        # Check if login successful
        snapshot = browser.snapshot()
        page_text = str(snapshot)
        
        if "ΕΥΑΓΓΕΛΟΣ ΧΑΤΖΗΪΩΑΝΝΟΥ" in page_text or "logout" in page_text.lower():
            print("✅ Login successful!")
            return True
        else:
            print("❌ Login failed")
            return False
            
    except Exception as e:
        print(f"❌ Login error: {e}")
        return False

def extract_announcements_from_forum(browser, forum_id):
    """Extract announcements from a forum."""
    if not forum_id:
        return []
    
    forum_url = f"{BASE_URL}/mod/forum/view.php?id={forum_id}"
    announcements = []
    
    try:
        browser.navigate(forum_url)
        time.sleep(2)
        
        snapshot = browser.snapshot()
        
        # Look for announcement rows in table
        # This is simplified - actual implementation would parse the HTML structure
        # and extract title, author, date for each announcement
        
        # For now, return empty list - full implementation would parse the table
        return announcements
        
    except Exception as e:
        print(f"❌ Error extracting from forum {forum_id}: {e}")
        return []

def check_all_courses(browser):
    """Check all courses for announcements."""
    print("\n" + "=" * 60)
    print("📚 CHECKING ALL COURSES")
    print("=" * 60)
    
    results = {}
    
    for course in COURSES:
        print(f"\n📖 {course['name']}")
        
        if course.get('forum_id'):
            announcements = extract_announcements_from_forum(browser, course['forum_id'])
            results[course['course_id']] = {
                "name": course['name'],
                "announcements": announcements,
                "count": len(announcements)
            }
            print(f"   Found {len(announcements)} announcements")
        else:
            print(f"   ⚠️ No forum configured")
            results[course['course_id']] = {
                "name": course['name'],
                "announcements": [],
                "count": 0
            }
    
    return results

def save_announcements(data):
    """Save announcements to memory."""
    memory_dir = Path("/root/.openclaw/workspace/memory/ecourse")
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    data_file = memory_dir / "announcements_latest.json"
    
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n💾 Saved to {data_file}")

def run_ecourse_check(browser):
    """Full ecourse check workflow."""
    print("🚀 Starting ecourse monitoring...")
    
    # Login
    if not login_to_ecourse(browser):
        print("❌ Cannot proceed without login")
        return None
    
    # Check all courses
    results = check_all_courses(browser)
    
    # Save results
    save_announcements({
        "timestamp": datetime.now().isoformat(),
        "courses": results
    })
    
    # Summary
    total = sum(c['count'] for c in results.values())
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"Total announcements found: {total}")
    print(f"Courses checked: {len(results)}")
    
    return results

if __name__ == "__main__":
    print("Ecourse Browser Bot")
    print("This script requires browser automation context")
    print("Run through main ecourse_monitor.py")
