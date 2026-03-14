# Auto-Git Commit Skill

**ID:** auto-git-commit  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw with git

---

## Purpose

Automatically commit and push changes to GitHub whenever files are modified, with descriptive commit messages and daily summaries.

## How It Works

### Architecture

```
File Modified / Heartbeat
  ↓
Check git status
  ↓
If changes detected:
  → Generate descriptive commit message
  → Stage changes
  → Commit with message
  → Push to GitHub
  → Verify push (hash check)
  ↓
Send Telegram confirmation
```

### Commit Message Format

```
[auto] Update 3 files in workspace/

- Modified: skills/cron-monitor/README.md
- Modified: memory/2026-03-14.md  
- Added: new-skill/SKILL.md

Auto-commit at 2026-03-14 14:30
```

### Batch Strategy

- **Immediate:** Critical files (SKILL.md, .py)
- **Batch:** Multiple small changes within 5 minutes
- **Daily:** Summary commit at 23:00

---

## Commands

### Manual Commit
```
"Commit my changes"
"Push to GitHub"
"Auto-commit now"
```

### Check Status
```
"Git status"
"What changed?"
"Show pending commits"
```

---

## Notifications

### Commit Success
```
✅ **AUTO-COMMIT SUCCESS**

📦 Committed: 3 files
📝 Message: [auto] Update skills
🔗 Hash: a1b2c3d
📤 Pushed to: origin/main
⏰ Time: 2026-03-14 14:30
```

### Daily Summary
```
📊 **GIT DAILY SUMMARY**

📦 Total Commits: 5
📄 Files Changed: 12
➕ Added: 3
✏️ Modified: 8
🗑️ Deleted: 1

🔗 Latest: c8d3d21
📅 Date: 2026-03-14
```

### Error Alert
```
❌ **AUTO-COMMIT FAILED**

⚠️ Error: Push rejected
🔧 Reason: Remote has newer changes
💡 Action: Manual pull required
```

---

## Configuration

```yaml
# config.yaml
auto_commit:
  enabled: true
  batch_minutes: 5
  commit_prefix: "[auto]"
  include_hash: true
  verify_push: true
  daily_summary: true
  daily_summary_time: "23:00"
  
exclude_patterns:
  - "*.tmp"
  - "*.log"
  - ".env"
  - "__pycache__/"
```

---

## Files

| File | Purpose |
|------|---------|
| `auto_git_commit.py` | Main automation logic |
| `commit_generator.py` | Descriptive message generator |
| `git_wrapper.py` | Safe git operations |
| `config.yaml` | Settings |

---

## Security

- Read-only by default
- Verify each push with hash check
- No force pushes
- Backup before major changes

---

## Version History

- **1.0.0** (2026-03-14) - Initial release
  - Automatic commit on file changes
  - Descriptive messages
  - Hash verification
  - Daily summaries
