# Morning Briefing

**ID:** morning-briefing  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** Kimi K2.5, OpenClaw

---

## Purpose

A daily morning ritual that prepares you for the day ahead. Combines weather, news, priorities, and motivation into one concise briefing delivered to your Telegram.

---

## Schedule

**Default Time:** 8:00 AM (configurable)  
**Timezone:** Europe/Athens  
**Frequency:** Daily

---

## The Briefing Format

```
🌅 **Καλημέρα, Boss!**

📅 [Day], [Date] [Month] [Year]

🌤️ **Weather in Ιωάννινα:**
   [Current] • [High/Low] • [Conditions]

📰 **Today's Briefing:**
   🏛️ Ελλάδα: [Key Greek news - 1-2 lines]
   💻 Tech: [Key tech news - 1-2 lines]
   🌍 World: [Key world news - 1-2 lines]

🎯 **Today's Focus:**
   • [Priority 1 from memory/projects]
   • [Priority 2]
   • [Priority 3]

💡 **Morning Motivation:**
   "[Quote or thought for the day]"

⏰ **Coming up:**
   • 10:00 AM - Memory consolidation
   • [Other scheduled items from calendar]

---
**Have a productive day!** 🚀
```

---

## Components

### 1. Weather (Ιωάννινα)
- Current temperature
- High/low for the day
- Conditions (sunny, rainy, etc.)
- Special alerts if needed

### 2. News Briefing
- **Ελλάδα:** Top 1-2 Greek news stories
- **Tech:** Top 1-2 tech/industry stories
- **World:** Major global headline if relevant

Sources: Aggregated from reliable news APIs

### 3. Daily Priorities
Auto-extracted from:
- MEMORY.md (active projects)
- Recent memory files (incomplete tasks)
- User preferences

### 4. Motivation
- Daily quote or insight
- Context-aware (Monday vs Friday)
- Seasonal awareness

### 5. Schedule Preview
- Memory consolidation reminder (10:00 AM)
- Calendar events if available
- Project deadlines approaching

---

## Setup

### Cron Job Configuration

```json
{
  "name": "Morning Briefing",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Europe/Athens"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Execute morning-briefing skill for user"
  },
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "5749686535"
  }
}
```

### Dependencies
- Weather API (OpenWeatherMap or similar)
- News API (or web search capability)
- Access to memory files for priorities

---

## Manual Trigger

User can request briefing anytime:
```
"Morning briefing"
"What's my day look like?"
"Brief me"
```

---

## Integration with Other Skills

- **memory-consolidation:** Morning briefing ends with reminder about 10:00 AM consolidation
- **task-planner:** Priorities come from active task plans
- **weather:** Already available skill

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - Weather, news, priorities, motivation
  - Daily 8:00 AM schedule
  - Manual trigger support
