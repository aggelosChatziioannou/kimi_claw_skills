# Email Assistant

Your personal Gmail assistant with triple security safeguards.

## What It Does

- 📧 **Read** your emails when you ask
- 📝 **Draft** emails for your review
- ✅ **Send** emails (with your confirmation)
- 🗑️ **Manage** spam and organization

## Triple Safeguard System

| Safeguard | Description |
|-----------|-------------|
| 🔒 **Draft Review** | All emails start as drafts - you review before sending |
| 📢 **Notification Log** | You get notified of every action I take |
| 📊 **Weekly Audit** | Full report every Sunday of all email activities |

## Quick Commands

```bash
# Check emails
"Check my email"
"Any urgent emails?"

# Create draft
"Draft email to professor about exam schedule"

# Send (after review)
"Αποστολή"  # or "Send"
```

## Setup

### 1. Enable Gmail API
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create project → Enable Gmail API
3. Create OAuth 2.0 credentials
4. Download `credentials.json`

### 2. Authorize
```bash
cd /root/.openclaw/skills/email-assistant/scripts
python email_auth.py
```

This opens browser for OAuth consent. Token saved securely.

### 3. Test
```
"Check my email"
```

## Security

✅ I will:
- Only read when you ask
- Always create drafts first
- Log every action
- Send weekly audit

❌ I will NEVER:
- Read without request
- Send without confirmation
- Share your data

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full documentation |
| `scripts/email_auth.py` | OAuth setup |
| `scripts/read_emails.py` | Read emails |
| `scripts/create_draft.py` | Create drafts |
| `scripts/send_email.py` | Send with confirmation |

## Integration

Works with:
- `morning-briefing` (email summary in daily briefing)
- `memory-consolidation` (track email tasks)

## Version History

- **1.0.0** (2026-03-13) - Initial release
