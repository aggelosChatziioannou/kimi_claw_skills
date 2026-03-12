# Email Assistant

**ID:** email-assistant  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw, Gmail API

---

## Purpose

Your personal email assistant that reads, drafts, and manages your Gmail with full transparency and security controls.

---

## Security Model (TRIPLE SAFEGUARD)

### 🔒 Safeguard #1: Draft Review
**ALL emails are created as DRAFTS first.**
- You review every email before sending
- I never send without your explicit "Αποστολή" / "Send"
- Drafts saved in Gmail drafts folder

### 🔒 Safeguard #2: Notification Log
**You get notified of EVERY email action:**
- "📧 Read 3 new emails"
- "📝 Created draft for [recipient]"
- "✅ Sent email to [recipient] (with your approval)"
- "🗑️ Marked 2 emails as spam"

### 🔒 Safeguard #3: Weekly Audit
**Every Sunday, you receive:**
```
📊 EMAIL AUDIT (Week of [date])

📧 Emails Read: 12
📝 Drafts Created: 3
✅ Emails Sent: 2
🗑️ Spam Cleared: 5

📋 Actions Log:
• [timestamp] Read email from [sender]
• [timestamp] Created draft for [recipient]
• [timestamp] Sent email to [recipient]
```

---

## Capabilities

### READ Mode
```
📧 Email Summary (Today):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 URGENT (needs reply):
   • Professor about exam schedule
   • Team project deadline reminder

🟡 IMPORTANT (read soon):
   • Newsletter: AI developments
   • Event invitation

⚪ NORMAL:
   • 5 promotional emails
   • Social media notifications
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### DRAFT Mode
```
📝 Creating draft for: professor@uni.gr
Subject: Question about exam schedule

[Draft content here]

⚠️ SAVED AS DRAFT - Review in Gmail
💬 Say "Αποστολή" when ready
```

### SEND Mode (with confirmation)
```
📤 Ready to send:
   To: professor@uni.gr
   Subject: Question about exam schedule
   
🤔 Confirm: "Αποστολή" or "Cancel"
```

---

## Commands

### Reading Emails
```
"Check my email"
"Τι emails έχω;"
"Any urgent emails?"
"Show unread emails"
```

### Creating Drafts
```
"Draft email to [name] about [topic]"
"Φτιάξε mail στον καθηγητή για [θέμα]"
"Reply to [sender] saying [message]"
```

### Managing Emails
```
"Mark [email] as read"
"Delete spam emails"
"Archive old newsletters"
"Search for [topic] in emails"
```

### Email Summary
```
"Email summary today"
"What did I receive today?"
"Any emails from [person]?"
```

---

## Gmail API Setup

### Step 1: Enable Gmail API
1. Go to https://console.cloud.google.com/
2. Create new project (or use existing)
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download `credentials.json`

### Step 2: OAuth Consent
1. Configure OAuth consent screen
2. Add scopes: `gmail.readonly`, `gmail.compose`, `gmail.modify`
3. Add test user: your email

### Step 3: First Run
```
python email_auth.py
# This will open browser for OAuth
# Save token.json for future use
```

---

## Privacy Promise

✅ **I will:**
- Only read emails when you ask
- Create drafts, not send immediately
- Log every action
- Respect your off-limits settings

❌ **I will NEVER:**
- Read emails without your request
- Send emails without confirmation
- Share your email content
- Store credentials insecurely

---

## File Structure

```
email-assistant/
├── SKILL.md                 # This file
├── README.md                # Quick start
├── scripts/
│   ├── email_auth.py        # OAuth setup
│   ├── read_emails.py       # Read functionality
│   ├── create_draft.py      # Draft creation
│   └── send_email.py        # Send (with confirmation)
└── memory/
    └── email-log.json       # Action audit log
```

---

## Integration with Morning Briefing

The morning briefing can include:
```
📧 Email Summary:
   • 3 new emails (1 needs reply)
   • 2 drafts waiting for your review
```

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - Gmail API integration
  - Triple safeguard system
  - Draft-first workflow
  - Audit logging
