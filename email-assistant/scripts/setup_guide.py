#!/usr/bin/env python3
"""
Email Assistant - Gmail OAuth Setup
Run this once to authorize Kimi-Claw to access your Gmail.
"""

print("""
╔═══════════════════════════════════════════════════════════════╗
║     EMAIL ASSISTANT - Gmail Authorization Setup              ║
╚═══════════════════════════════════════════════════════════════╝

🔐 STEP 1: Google Cloud Console Setup
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Go to: https://console.cloud.google.com/
2. Create a new project (or select existing)
3. Enable the Gmail API:
   - APIs & Services → Library
   - Search "Gmail API"
   - Click "Enable"

4. Create OAuth 2.0 Credentials:
   - APIs & Services → Credentials
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "Kimi-Claw Email Assistant"
   - Click "Create"
   - Download the JSON file

5. Configure OAuth Consent Screen:
   - APIs & Services → OAuth consent screen
   - User Type: "External"
   - App name: "Kimi-Claw Email Assistant"
   - User support email: [your email]
   - Developer contact: [your email]
   - Scopes: Add these:
     • https://www.googleapis.com/auth/gmail.readonly
     • https://www.googleapis.com/auth/gmail.compose
     • https://www.googleapis.com/auth/gmail.modify
   - Add your email as "Test user"
   - Publish status: "Testing" (sufficient for personal use)

🔐 STEP 2: Save Credentials
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Save the downloaded JSON as:
/root/.openclaw/skills/email-assistant/credentials.json

🔐 STEP 3: Run Authorization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tell Kimi-Claw: "Run email authorization"

This will:
1. Open browser for Google sign-in
2. Request permission for Gmail access
3. Save token securely for future use

🔐 STEP 4: Test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Say: "Check my email"

If setup is correct, you'll see your email summary!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 TIP: The token is saved securely and refreshed automatically.
    You only need to do this setup once!

🛡️  SECURITY: Your credentials are stored locally only.
    Kimi-Claw never shares your email data.

""")
