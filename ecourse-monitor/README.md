# Ecourse Monitor

Automatic monitoring of UOI ecourse announcements.

## What It Does

📚 **Monitors all your courses** (9 courses)  
🔔 **Checks for new announcements** every 6 hours  
📊 **Morning briefing** with summary  
📱 **Telegram notifications** for new announcements  
📈 **Tracks history** of all announcements  

## Features

### 1. Automatic Course Monitoring
- Checks all 9 enrolled courses
- Extracts announcements from each course forum
- Saves to local database

### 2. New Announcement Detection
- Compares with previous check
- Identifies new announcements
- Sends immediate notification

### 3. Morning Briefing Integration
```
📚 **ECOURSE CHECK**

🔔 Νέες ανακοινώσεις (2):

1. **Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας**
   • "Ωράριο Διαλέξεων" - ΕΥΑΓΓΕΛΟΣ ΚΟΣΙΝΑΣ
   • Δευ, 16 Φεβ 2026

2. **Δίκτυα Υπολογιστών**
   • "Εργασία #2" - Καθηγητής
   • Σήμερα, 09:00
```

### 4. Data Persistence
- All announcements saved to memory
- Course information stored
- Check history logged

## Monitored Courses

1. ΜΥΕ017 Κατανεμημένα Συστήματα
2. Αλγόριθμοι για Δεδομένα Ευρείας Κλίμακας
3. Διακριτά Μαθηματικά ΙI
4. Διδακτική της Πληροφορικής
5. Δίκτυα Υπολογιστών I (MYY703)
6. Εξόρυξη δεδομένων
7. ΜΙΚΡΟΕΠΕΞΕΡΓΑΣΤΕΣ
8. Προχωρημένα Θέματα Τεχνολογίας και Εφαρμογών Βάσεων
9. Υπολογιστική Όραση

## How It Works

```
Cron Job (every 6 hours)
↓
Login to ecourse
↓
For each course:
  → Navigate to announcements forum
  → Extract all announcements
  → Compare with stored data
  → Identify new announcements
↓
If new announcements found:
  → Send Telegram notification
  → Update morning briefing data
↓
Save all data to memory
```

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

## Files

- `ecourse_monitor.py` - Main monitoring script
- `courses.json` - Course list and URLs
- `announcements.json` - All announcements database
- `config.yaml` - Login credentials (encrypted)

## Version

1.0.0 (2026-03-14)
