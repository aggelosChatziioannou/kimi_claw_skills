# Auto-Documentation - Generate Docs from Code

## Purpose
Automatically generate documentation from code - README, API docs, changelogs.

## Why This Skill Exists
Documentation is always outdated. This skill reads the actual code and generates fresh docs automatically.

## Features

### 1. 📄 README Generator
**Analyzes:**
- Project structure
- Technologies used
- Main files and purpose
- Dependencies

**Generates:**
- Professional README.md
- Installation instructions
- Usage examples
- Feature list
- Badges (license, version, etc.)

---

### 2. 🔌 API Documenter
**Analyzes:**
- Route definitions
- Request/response types
- Parameters
- Authentication

**Generates:**
- API endpoint documentation
- Example requests/responses
- Error codes
- Postman collection (optional)

---

### 3. 📝 Changelog Creator
**Analyzes:**
- Git commit history
- Commit messages
- Tags/releases

**Generates:**
- CHANGELOG.md
- Version history
- Breaking changes
- What's new

---

### 4. 🧩 Function Documenter
**Analyzes:**
- Function signatures
- Parameters and types
- Return values
- Comments in code

**Generates:**
- Inline documentation
- JSDoc/TSDoc comments
- Function reference

---

## Usage

```
"Φτιάξε μου README για αυτό το project"
"Generate API documentation"
"Create changelog from commits"
"Document this codebase"
```

## Output Formats

### README.md Template
```markdown
# Project Name

## 🚀 Features
- Feature 1
- Feature 2

## 📦 Installation
```bash
npm install
```

## 🛠️ Usage
```javascript
// Example code
```

## 📚 API Reference
[Link to API docs]

## 📄 License
MIT
```

### API Documentation Template
```markdown
## API Endpoints

### GET /api/users
**Description:** Get all users

**Parameters:**
- limit (number, optional) - Max results
- offset (number, optional) - Pagination

**Response:**
```json
{
  "users": [...],
  "total": 100
}
```

**Errors:**
- 401 - Unauthorized
- 500 - Server error
```

### Changelog Template
```markdown
# Changelog

## [1.2.0] - 2026-03-13
### Added
- New feature X
- Support for Y

### Fixed
- Bug in Z
- Performance issue

## [1.1.0] - 2026-02-28
...
```

## Process

### Step 1: Scan Project
```
📁 Analyzing project structure...
├── Found: package.json (Node.js project)
├── Found: Next.js framework
├── Found: TypeScript
└── Found: 5 API routes
```

### Step 2: Extract Information
```
📊 Extracting data...
✓ Main entry: src/index.ts
✓ Framework: Next.js 15
✓ Language: TypeScript
✓ Styling: Tailwind CSS
✓ Database: PostgreSQL
```

### Step 3: Generate Documentation
```
✍️ Writing README.md...
✍️ Writing API.md...
✍️ Writing CHANGELOG.md...
```

### Step 4: Review & Deliver
```
📋 Generated:
✓ README.md (comprehensive)
✓ API.md (12 endpoints documented)
✓ CHANGELOG.md (last 3 months)
```

## Examples

### Example 1: E-Shop Project
```
Input: Project with products, cart, checkout

Output README.md:
---
# E-Shop Platform

Modern e-commerce platform built with Next.js

## ✨ Features
- 🛍️ Product catalog with search
- 🛒 Shopping cart
- 💳 Stripe payment integration
- 👤 User authentication
- 📱 Mobile responsive

## 🚀 Tech Stack
- Next.js 15
- TypeScript
- Tailwind CSS
- Prisma ORM
- PostgreSQL

## 📦 Installation
1. Clone repo
2. npm install
3. cp .env.example .env
4. npm run dev

## 🔌 API Endpoints
- GET /api/products
- POST /api/cart
- POST /api/checkout
...
---
```

### Example 2: API Documentation
```
Input: Express.js API

Output API.md:
---
## Authentication

### POST /api/auth/login
Login with email and password

**Request:**
```json
{
  "email": "user@example.com",
  "password": "secret"
}
```

**Response:**
```json
{
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "email": "user@example.com"
  }
}
```

**Errors:**
- 400 - Invalid credentials
- 422 - Validation error
---
```

## Benefits

✅ **Always up-to-date** - Generated from actual code
✅ **Consistent format** - Standard structure
✅ **Time saving** - No manual writing
✅ **Complete coverage** - Nothing forgotten
✅ **Professional** - Clean, readable docs

---
Last Updated: 2026-03-13
Status: Active
