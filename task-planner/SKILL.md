# Task Planner - Smart Project Breakdown

## Purpose
Break large, overwhelming projects into small, manageable, actionable steps.

## Why This Skill Exists
Big projects feel impossible. Task Planner creates a clear roadmap so you always know what to do next.

## How It Works

### Input
User describes a project: "Φτιάξε μου ένα e-shop" ή "Build a mobile app"

### Output
Structured plan with:
- Phases (high-level stages)
- Tasks (specific actions)
- Estimates (time for each step)
- Dependencies (what needs to happen first)

## Planning Process

### Step 1: Analyze Project Type
Identify the category:
- Web Application
- Mobile App
- API/Backend
- Documentation
- Automation
- Research

### Step 2: Define Phases
Typical phases for web app:
```
Phase 1: Setup & Planning (Day 1)
Phase 2: Design System (Day 1-2)
Phase 3: Core Development (Day 2-5)
Phase 4: Testing (Day 5-6)
Phase 5: Deployment (Day 6-7)
```

### Step 3: Break Into Tasks
Each phase → specific tasks:
```
Phase 3: Core Development
├── Task 3.1: Setup project structure
├── Task 3.2: Build authentication
├── Task 3.3: Create database schema
├── Task 3.4: Build main pages
├── Task 3.5: Add API endpoints
└── Task 3.6: Connect frontend-backend
```

### Step 4: Identify Dependencies
```
Task 3.2 (Auth) depends on Task 3.1 (Setup)
Task 3.6 (Connect) depends on Task 3.4 and 3.5
```

### Step 5: Estimate Time
```
Task 3.1: 30 min
Task 3.2: 2 hours
Task 3.3: 1 hour
Task 3.4: 4 hours
Task 3.5: 3 hours
Task 3.6: 2 hours
```

## Output Format

```
🎯 PROJECT: [Name]
⏱️ TOTAL ESTIMATE: [X hours/days]

═══════════════════════════════════════

📋 PHASE 1: [Name] ([Duration])
├── [ ] Task 1.1: [Description] (~X min)
├── [ ] Task 1.2: [Description] (~X min)
└── [ ] Task 1.3: [Description] (~X min)

📋 PHASE 2: [Name] ([Duration])
├── [ ] Task 2.1: [Description] (~X min)
│   └── 🔗 Depends on: Task 1.2
├── [ ] Task 2.2: [Description] (~X min)
└── [ ] Task 2.3: [Description] (~X min)

[... more phases ...]

═══════════════════════════════════════

🚀 NEXT ACTION: Start with Task 1.1
💡 TIP: [Specific advice for this project]
```

## Special Features

### Auto-Detection
Recognizes project type from description:
- "website", "site" → Web Application
- "app", "mobile" → Mobile App
- "API", "backend" → API/Backend
- "report", "research" → Research Project

### Realistic Estimates
Based on project type and complexity:
- Simple: 1-3 days
- Medium: 1-2 weeks
- Complex: 1-3 months

### Dependency Management
Shows what needs to happen first:
- Setup → Development
- Design → Implementation
- Backend → Frontend connection
- Testing → Deployment

### Progress Tracking
Check off completed tasks:
```
├── [✓] Task 1.1: Setup project (Done)
├── [ ] Task 1.2: Configure tools (Next)
└── [ ] Task 1.3: Create repo
```

## Examples

### Example 1: E-Shop
```
User: "Φτιάξε μου ένα e-shop"

🎯 PROJECT: E-Shop (Next.js + Stripe)
⏱️ TOTAL ESTIMATE: 5-7 days

📋 PHASE 1: Setup (Day 1)
├── [ ] Task 1.1: Initialize Next.js project
├── [ ] Task 1.2: Setup Tailwind CSS
├── [ ] Task 1.3: Configure ESLint/Prettier
└── [ ] Task 1.4: Create GitHub repo

📋 PHASE 2: Design (Day 1-2)
├── [ ] Task 2.1: Create wireframes
├── [ ] Task 2.2: Design database schema
└── [ ] Task 2.3: Setup shadcn/ui components

📋 PHASE 3: Development (Day 2-5)
├── [ ] Task 3.1: Build product pages
├── [ ] Task 3.2: Create shopping cart
├── [ ] Task 3.3: Integrate Stripe payments
└── [ ] Task 3.4: Add user authentication

📋 PHASE 4: Testing (Day 5-6)
├── [ ] Task 4.1: Test payment flow
├── [ ] Task 4.2: Mobile responsiveness
└── [ ] Task 4.3: Performance optimization

📋 PHASE 5: Deployment (Day 6-7)
├── [ ] Task 5.1: Setup Vercel
├── [ ] Task 5.2: Configure domain
└── [ ] Task 5.3: Go live

🚀 NEXT ACTION: Task 1.1 - Initialize project
```

### Example 2: Research Report
```
User: "Κάνε μου έρευνα για AI trends 2026"

🎯 PROJECT: AI Trends Research Report
⏱️ TOTAL ESTIMATE: 3-4 hours

📋 PHASE 1: Planning (15 min)
├── [ ] Task 1.1: Define research scope
├── [ ] Task 1.2: Identify key topics
└── [ ] Task 1.3: Plan source strategy

📋 PHASE 2: Research (1-2 hours)
├── [ ] Task 2.1: Search current trends
├── [ ] Task 2.2: Find expert opinions
├── [ ] Task 2.3: Gather statistics
└── [ ] Task 2.4: Cross-reference sources

📋 PHASE 3: Analysis (30-45 min)
├── [ ] Task 3.1: Identify patterns
├── [ ] Task 3.2: Compare findings
└── [ ] Task 3.3: Spot gaps

📋 PHASE 4: Writing (30-45 min)
├── [ ] Task 4.1: Write executive summary
├── [ ] Task 4.2: Document key findings
├── [ ] Task 4.3: Add sources
└── [ ] Task 4.4: Format report

🚀 NEXT ACTION: Task 1.1 - Define scope
```

## Usage

```
"Φτιάξε μου plan για [project]"
"Task planner: [project description]"
"Κάνε breakdown το [project]"
"Plan this project: [description]"
```

## Integration with Other Skills

### With Deep Research
1. Task Planner: Break research into phases
2. Deep Research: Execute each phase with live updates

### With Communication Protocol
1. Task Planner: Show overall roadmap
2. Execute: Status updates for each task

### With Self-Review
1. After each task: Review quality
2. Check off: Mark as complete

## Benefits

✅ **No overwhelm** - Clear, small steps
✅ **Progress tracking** - See what's done
✅ **Time estimates** - Know how long it takes
✅ **Dependencies** - Do things in right order
✅ **Focus** - Always know next action

---
Last Updated: 2026-03-13
Status: Active
