#!/usr/bin/env python3
"""
Email Assistant - Gmail OAuth Authentication
Run this to authorize Kimi-Claw to access your Gmail.
"""

import os
import json
from pathlib import Path

# Note: In production, this would use google-auth and google-auth-oauthlib
# For now, we provide the setup instructions

CREDENTIALS_PATH = Path("/root/.openclaw/skills/email-assistant/credentials.json")
TOKEN_PATH = Path("/root/.openclaw/skills/email-assistant/token.json")

def check_prerequisites():
    """Check if credentials file exists."""
    if not CREDENTIALS_PATH.exists():
        print("""
❌ CREDENTIALS NOT FOUND

You need to:
1. Go to https://console.cloud.google.com/
2. Create a project and enable Gmail API
3. Create OAuth 2.0 credentials (Desktop app)
4. Download credentials.json
5. Save it to: /root/.openclaw/skills/email-assistant/credentials.json

Run: python setup_guide.py for detailed instructions.
""")
        return False
    return True

def authenticate():
    """
    OAuth authentication flow.
    In production, this opens browser for user consent.
    """
    if not check_prerequisites():
        return
    
    print("""
🔐 GMAIL AUTHORIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ credentials.json found!

To complete authorization, you need to run the OAuth flow:

OPTION 1: Automatic (if google-auth is installed)
-------------------------------------------------
The script would:
1. Open your browser
2. Ask you to sign in to Google
3. Grant permission to Kimi-Claw Email Assistant
4. Save token.json automatically

OPTION 2: Manual Token Creation
-------------------------------
If automatic doesn't work:

1. Go to: https://developers.google.com/oauthplayground
2. Click the gear icon (⚙️) → Check "Use your own OAuth credentials"
3. Enter your Client ID and Secret from credentials.json
4. Select scopes:
   • https://www.googleapis.com/auth/gmail.readonly
   • https://www.googleapis.com/auth/gmail.compose
   • https://www.googleapis.com/auth/gmail.modify
5. Click "Authorize APIs"
6. Exchange authorization code for tokens
7. Save the refresh_token

Then create token.json:
{
  "token": "ya29...",
  "refresh_token": "1//...",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "scopes": [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.modify"
  ]
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def install_dependencies():
    """Check and install required packages."""
    print("""
📦 DEPENDENCIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Required packages:
  pip install google-auth google-auth-oauthlib google-auth-httplib2
  pip install google-api-python-client

Run the above command to install Gmail API dependencies.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        install_dependencies()
    else:
        authenticate()
