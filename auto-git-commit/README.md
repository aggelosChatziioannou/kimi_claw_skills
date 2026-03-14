# 🤖 Auto-Git Commit Skill

**Skill #33** - Automatic git commit and push with descriptive messages

---

## 📋 Overview

This skill automatically commits and pushes your changes to GitHub with smart, descriptive commit messages. Never lose work again!

## 🎯 Features

- ✅ **Automatic Commits** - On file changes or schedule
- 📝 **Smart Messages** - Descriptive commit messages
- 🔗 **Hash Verification** - Confirms push success
- 📤 **Auto-Push** - Pushes to origin/main
- 📊 **Daily Summaries** - Activity reports
- 🚫 **Safe Operations** - No force pushes

## 📝 Commit Message Format

```
[auto] Update 3 skill files

➕ Added 1:
  • new-skill/SKILL.md

✏️ Modified 2:
  • cron-monitor/README.md
  • cron-monitor/cron_monitor.py

⏰ Auto-commit at 2026-03-14 14:30
```

## 📱 Example Notifications

### Commit Success
```
✅ **AUTO-COMMIT SUCCESS**

📦 Committed: 3 files
🔗 Hash: `a1b2c3d`
📤 Pushed to: origin/main
✅ Verified: Local = Remote
⏰ Time: 2026-03-14 14:30
```

### Daily Summary
```
📊 **GIT DAILY SUMMARY**

📦 Total Commits: 5
📄 Files Changed: 12
➕ Insertions: +245
🗑️ Deletions: -18
🔗 Latest: `c8d3d21`
📅 Date: 2026-03-14
```

### No Changes
```
ℹ️ **AUTO-COMMIT**

No changes to commit
```

## 🛠️ Commands

```
"Commit my changes"
"Push to GitHub"
"Auto-commit now"
"Git status"
"What changed?"
```

## ⏰ Automatic Schedule

- **On file changes:** Immediate for critical files
- **Batch window:** 5 minutes for multiple changes
- **Daily summary:** 23:00 (Europe/Athens)

## 📁 Files

```
auto-git-commit/
├── SKILL.md              # Technical documentation
├── README.md             # This file
├── auto_git_commit.py    # Main logic
└── __init__.py
```

## 🔧 Configuration

Edit in `auto_git_commit.py`:

```python
FILE_CATEGORIES = {
    "skill": ["SKILL.md", "/skills/"],
    "memory": ["memory/", "MEMORY.md"],
    "code": [".py", ".js", ".ts"],
    "docs": [".md", ".txt"],
}
```

## 🛡️ Safety Features

- ✅ Hash verification after push
- ✅ No force pushes
- ✅ Detailed error messages
- ✅ Dry-run mode available

## 📝 Version History

- **1.0.0** (2026-03-14) - Initial release

---

*Made with ❤️‍🔥 by Kimi Claw*
