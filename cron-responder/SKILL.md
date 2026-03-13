# Cron Responder

**ID:** cron-responder  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw, Telegram

---

## Purpose

Automatically respond to cron system events and forward messages to Telegram. Acts as a bridge between cron jobs and user notifications.

---

## How It Works

When a cron job fires with `sessionTarget: "main"` and `payload.kind: "systemEvent"`, this skill:
1. Receives the system event text
2. Identifies the event type (morning brief, memory consolidation, etc.)
3. Generates appropriate message content
4. Sends directly to user's Telegram

---

## Event Types

### Morning Briefing
**Trigger:** `🌅 MORNING BRIEFING`
**Action:** Generate and send daily briefing with weather, news, priorities

### Memory Consolidation  
**Trigger:** `🧠 DAILY MEMORY CONSOLIDATION`
**Action:** Generate and send memory summary

### Custom Events
**Trigger:** Any text starting with emoji identifier
**Action:** Parse and respond appropriately

---

## Usage

Set up cron job with systemEvent:
```json
{
  "name": "Morning Briefing",
  "schedule": {
    "kind": "cron", 
    "expr": "0 8 * * *",
    "tz": "Europe/Athens"
  },
  "sessionTarget": "main",
  "payload": {
    "kind": "systemEvent",
    "text": "🌅 MORNING BRIEFING"
  }
}
```

When event fires, this skill automatically:
1. Detects "🌅 MORNING BRIEFING" 
2. Generates briefing content
3. Sends to Telegram via message tool

---

## Response Format

On receiving system event, respond immediately with:
```
message:send → channel: telegram → to: [user_id]
```

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - Handle morning briefing events
  - Handle memory consolidation events
  - Telegram forwarding
