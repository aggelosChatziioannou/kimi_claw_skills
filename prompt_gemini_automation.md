# GEMINI AUTOMATION SCHEDULING - DETAILED PROMPT FOR EXTERNAL AI MODEL

## EXECUTIVE SUMMARY

**Request:** Design a robust, production-ready solution for automating Google Gemini image generation with persistent authentication on a headless Linux server, scheduled to run via cron jobs.

**Current System:** Kimi Claw (OpenClaw agent) - An AI assistant running inside OpenClaw framework with Playwright-based browser automation capabilities.

---

## SYSTEM CONTEXT

### What is Kimi Claw / OpenClaw?

**Kimi Claw** is an AI assistant (similar to Claude or GPT) that runs inside the **OpenClaw** framework. OpenClaw provides:

- **Browser automation** via Playwright (through `browser` tool)
- **File system access** (read/write/execute)
- **Cron job scheduling** (via `cron` tool with isolated agent sessions)
- **Telegram integration** (messaging)
- **Shell command execution**
- **Python/Node.js execution**

**Constraints:**
- Runs on a headless Linux server (no GUI)
- Cannot use headed Chrome (must use headless or xvfb)
- Cannot easily persist interactive sessions across cron runs
- Has limited direct cookie/credential injection capabilities

### Target Task

Create a scheduled automation that:
1. **Logs into Google Gemini** (or maintains persistent login)
2. **Generates an image** with prompt "nano banana"
3. **Downloads the image**
4. **Uploads to GitHub repository**
5. **Runs on a schedule** (e.g., daily at specific time)

---

## ATTEMPTED APPROACHES & FAILURES

### ATTEMPT 1: Cookie-Based Authentication (FAILED)

**Method:**
- User exported cookies from Chrome using Cookie-Editor extension
- Cookies saved as JSON file
- Attempted to inject cookies into Playwright context

**Code Attempted:**
```python
import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    # Load cookies from JSON
    with open('cookies.json', 'r') as f:
        cookies = json.load(f)
    
    # Add cookies to context
    context.add_cookies(cookies)
    
    page = context.new_page()
    page.goto("https://gemini.google.com")
```

**Why it Failed:**
- OpenClaw's browser tool doesn't support direct cookie import from JSON
- Chrome cookies are OS-level encrypted (Windows credentials don't transfer to Linux)
- Session cookies expire or become invalid when moved between machines
- Google detects cookie tampering and invalidates the session

**Error Messages:**
- "Sign in" button still appeared after cookie injection
- Session not recognized as authenticated

---

### ATTEMPT 2: Chrome Profile Export/Import (FAILED)

**Method:**
- User exported entire Chrome profile directory from Windows
- Profile zipped and uploaded to Linux server
- Used Playwright's `launch_persistent_context()` with custom user data directory

**Code Attempted:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="/root/chrome-profile-gemini",
        channel="chrome",
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    page = context.new_page()
    page.goto("https://gemini.google.com")
```

**Why it Failed:**
- Chrome profile encryption is OS-specific (Windows DPAPI doesn't work on Linux)
- The `Login Data`, `Cookies`, and `Secure Preferences` files are encrypted with Windows user credentials
- When loaded on Linux, Chrome sees the profile as corrupted/invalid
- Google services require re-authentication

**Evidence:**
- Screenshot showed "Sign in" button still present
- Profile loaded but authentication state not preserved

---

### ATTEMPT 3: Automated Login with Stealth (PARTIALLY WORKED, NOT RELIABLE)

**Method:**
- Fresh Chrome profile on Linux
- Automated typing of credentials with human-like delays
- Attempted 2FA completion

**Code Attempted:**
```python
from playwright.sync_api import sync_playwright
import random

EMAIL = "aggeloshatzioannou@gmail.com"
PASSWORD = "[REDACTED]"

def human_delay():
    time.sleep(random.uniform(0.5, 1.5))

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        "/root/chrome-profile-gemini-linux",
        channel="chrome",
        headless=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
        args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
    )
    
    page = context.new_page()
    page.goto("https://accounts.google.com/signin")
    
    # Enter email with human-like typing
    email_input = page.locator("input[type='email']").first
    for char in EMAIL:
        email_input.type(char, delay=random.randint(50, 150))
    email_input.press("Enter")
    
    # Enter password
    password_input = page.locator("input[type='password']").first
    for char in PASSWORD:
        password_input.type(char, delay=random.randint(50, 150))
    password_input.press("Enter")
```

**Partial Success:**
- ✅ Email entry: SUCCESS
- ✅ Password entry: SUCCESS
- ✅ Reached 2FA screen: SUCCESS
- ❌ Session persistence: FAILED (session expired before 2FA completed)

**Why it's Not Suitable for Scheduling:**
- 2FA requires real-time human interaction (user must tap "50" on phone)
- Google Prompt approval is time-sensitive (expires after ~30 seconds)
- Cron jobs run in isolated sessions - cannot wait for human input
- Each cron run would require fresh 2FA approval - not autonomous

**Google's Anti-Automation Measures Encountered:**
- "Sign in rejected" pages
- Rate limiting after multiple attempts
- Detection of headless Chrome
- Changed flow URLs (rejected state)
- CAPTCHA challenges (not reached but likely)

---

## PROBLEM ANALYSIS

### Core Challenges

1. **Authentication Persistence**
   - Google uses multiple layers of security (password + 2FA + device trust)
   - Sessions are bound to specific device fingerprints
   - Moving authentication across machines invalidates sessions

2. **Headless Environment**
   - No GUI for interactive login
   - Cannot use headed Chrome for one-time setup
   - xvfb possible but adds complexity

3. **Scheduling Requirements**
   - Must run autonomously without human intervention
   - Cannot wait for 2FA prompts during cron execution
   - Need persistent authentication across days/weeks

4. **Google's Bot Detection**
   - Chrome Headless detection
   - Automation pattern recognition
   - IP-based rate limiting
   - Behavioral analysis

### What We Have Available

**System Capabilities:**
- Python 3.12 with Playwright installed
- Node.js available
- Chrome/Chromium installed
- Cron scheduling via OpenClaw
- Telegram messaging for notifications
- File system persistence

**User Resources:**
- Google account with 2FA enabled (phone prompt)
- GitHub account for image upload
- Willing to set up API keys if needed

---

## REQUEST FOR SOLUTION

Design a **production-ready, scheduled automation system** for Google Gemini image generation that addresses:

### REQUIREMENTS (Must Have)

1. **Persistent Authentication**
   - Login once, use for weeks/months
   - No human intervention required per run
   - Handle token refresh automatically

2. **Cron-Compatible**
   - Runs entirely headless
   - Completes within reasonable time (5-10 minutes max)
   - No interactive prompts during execution

3. **Reliability**
   - Error handling and retry logic
   - Graceful degradation
   - Status reporting (success/failure)

4. **Security**
   - Credentials stored securely (not hardcoded)
   - No plaintext passwords in scripts

### NICE TO HAVE

- Image upload to GitHub with automatic commits
- Telegram notification on success/failure
- Multiple image generation prompts
- Logging and monitoring

---

## POTENTIAL APPROACHES TO EVALUATE

### Option A: Google AI Studio API

**Idea:** Use official Google API instead of browser automation

**Pros:**
- Officially supported
- No browser automation headaches
- Designed for programmatic access
- Better reliability

**Cons:**
- May have different capabilities than web Gemini
- Rate limits
- Requires API key management

**Questions:**
- Does AI Studio API support image generation with the same quality as web Gemini?
- What are the rate limits?
- Is there a free tier sufficient for daily use?

### Option B: OAuth 2.0 with Refresh Tokens

**Idea:** Use Google's OAuth flow with offline access to get refresh tokens

**Pros:**
- Official authentication method
- Can persist across sessions
- No browser automation needed after initial setup

**Cons:**
- Complex initial setup
- Requires Google Cloud project
- May not work for Gemini specifically (depends on API availability)

### Option C: Browser Automation with Session Persistence

**Idea:** Use Playwright with advanced stealth and session persistence

**Approaches:**
1. **CDP (Chrome DevTools Protocol) connection** to persistent Chrome instance
2. **Playwright with saved storage state** (cookies + localStorage)
3. **Session relay** through a always-on browser instance

**Pros:**
- Full web Gemini capabilities
- No API limitations

**Cons:**
- Complex to maintain
- Still subject to bot detection
- Session may still expire

### Option D: Third-Party API Services

**Idea:** Use services like:
- ScrapingBee
- ScraperAPI
- Browserless

**Pros:**
- Handle proxy rotation
- Built-in stealth
- Managed infrastructure

**Cons:**
- Additional cost
- May still have issues with Google authentication

---

## QUESTIONS FOR THE SOLUTION

Please provide a solution that answers:

1. **Which approach do you recommend and why?**

2. **Step-by-step implementation guide:**
   - Prerequisites
   - Initial setup (one-time)
   - Daily automation script
   - Cron configuration

3. **Code implementation:**
   - Complete working Python script
   - Error handling
   - Logging
   - Configuration management

4. **Authentication strategy:**
   - How to obtain and store credentials/tokens
   - How to refresh when needed
   - Security best practices

5. **Maintenance and monitoring:**
   - How to detect failures
   - How to re-authenticate if needed
   - Logging and alerting

6. **Alternative approaches:**
   - If primary approach fails, what are the backups?

---

## ADDITIONAL CONTEXT

**Environment Details:**
- OS: Linux (Ubuntu/Debian based)
- Python: 3.12
- Playwright: Installed with Chromium
- Network: Standard internet connection
- Storage: Persistent filesystem at `/root/`

**User's Google Account:**
- Has 2FA enabled (phone prompt)
- Regular consumer account (not Workspace/Enterprise)
- Location: Greece (Europe/Athens timezone)

**Previous Automation Experience:**
- Successfully automated ecourse.uoi.gr (university portal)
- Successfully automated various other websites
- Has 33+ custom skills in OpenClaw
- Experience with cron jobs and scheduling

**Acceptable Trade-offs:**
- User can perform one-time setup steps manually
- Can use API keys if they provide better reliability
- Can use third-party services if cost-effective
- Willing to use alternative AI image generators if Gemini proves impossible

---

## DELIVERABLES EXPECTED

Please provide:

1. **Recommended solution** with clear justification
2. **Complete implementation code** (Python preferred)
3. **Setup instructions** (step-by-step)
4. **Configuration examples** (with placeholders for sensitive data)
5. **Troubleshooting guide** (common issues and solutions)
6. **Alternative options** (if primary solution is not viable)

---

## NOTE TO AI MODEL

This is a challenging problem that requires balancing:
- Security (Google's anti-automation measures)
- Reliability (cron-scheduled automation)
- Practicality (production-ready solution)

The user has already invested significant effort and is looking for an expert-level solution that actually works in production, not just proof-of-concept.

Please be thorough, consider edge cases, and provide a solution that can be deployed and maintained long-term.

Thank you!
