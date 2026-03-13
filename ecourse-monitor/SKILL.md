# Ecourse Monitor Skill

**ID:** ecourse-monitor  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw with browser automation

---

## Purpose

Automatically monitor UOI ecourse platform for new announcements in enrolled courses.

## How It Works

### Architecture

```
Cron Job (every 6 hours)
  ↓
Browser Automation
  ↓
Login to ecourse
  ↓
For each of 9 courses:
  → Navigate to course
  → Find announcements forum
  → Extract all announcements
  → Compare with stored data
  ↓
If new announcements:
  → Send Telegram notification
  → Update morning briefing data
  ↓
Save to memory
```

### Data Structure

```json
{
  "last_check": "2026-03-14T02:30:00",
  "courses": {
    "4384": [
      {
        "id": "ann_001",
        "title": "Ωράριο Διαλέξεων",
        "author": "ΕΥΑΓΓΕΛΟΣ ΚΟΣΙΝΑΣ",
        "date": "2026-02-16T11:46:00",
        "url": "..."
      }
    ]
  }
}
```

---

## Monitored Courses

| # | Course Name | Course ID |
|---|-------------|-----------|
| 1 | ΜΥΕ017 Κατανεμημένα Συστήματα | 4384 |
| 2 | Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας | 2114 |
| 3 | Διακριτά Μαθηματικά ΙI | 3097 |
| 4 | Διδακτική της Πληροφορικής | 1916 |
| 5 | Δίκτυα Υπολογιστών I (MYY703) | 869 |
| 6 | Εξόρυξη δεδομένων | 1024 |
| 7 | ΜΙΚΡΟΕΠΕΞΕΡΓΑΣΤΕΣ | 1823 |
| 8 | Προχωρημένα Θέματα Τεχνολογίας και Εφαρμογών Βάσεων | 2194 |
| 9 | Υπολογιστική Όραση | 1678 |

---

## Commands

### Manual Check
```
"Check ecourse announcements"
"Τσέκαρε το ecourse"
"Any new announcements?"
```

### Get Summary
```
"Show my ecourse summary"
"Τι ανακοινώσεις έχω;"
```

---

## Notifications

### New Announcement Alert
```
📚 **ΝΕΕΣ ΑΝΑΚΟΙΝΩΣΕΙΣ ECOURSE**

🔔 Βρέθηκαν 2 νέες ανακοινώσεις:

**Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας**
📌 Ωράριο Διαλέξεων
👤 ΕΥΑΓΓΕΛΟΣ ΚΟΣΙΝΑΣ
📅 Δευ, 16 Φεβ 2026

**Δίκτυα Υπολογιστών**
📌 Εργασία #2
👤 Καθηγητής
📅 Σήμερα, 09:00
```

### Morning Briefing
```
📚 **ECOURSE CHECK**

📊 Σύνολο: 15 ανακοινώσεις σε 3 μαθήματα

**Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας** (2 ανακοινώσεις)
  • Ωράριο Διαλέξεων

**ΜΥΕ017 Κατανεμημένα Συστήματα** (1 ανακοίνωση)
  • Διαδικαστικά μαθήματος

⏱️ Τελευταίος έλεγχος: 2026-03-14 08:00
```

---

## Cron Schedule

```json
{
  "schedule": {
    "hours": [6, 12, 18, 0],
    "timezone": "Europe/Athens"
  }
}
```

---

## Files

| File | Purpose |
|------|---------|
| `ecourse_monitor.py` | Main monitoring logic |
| `browser_bot.py` | Browser automation |
| `courses.json` | Course configuration |
| `announcements.json` | Stored announcement data |

---

## Security

- Credentials stored encrypted
- Session cookies managed securely
- No password logging

---

## Version History

- **1.0.0** (2026-03-14) - Initial release
  - 9 course monitoring
  - Browser automation
  - Telegram notifications
  - Morning briefing integration
