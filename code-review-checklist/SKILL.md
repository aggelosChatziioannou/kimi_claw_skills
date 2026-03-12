# Code Review Checklist - Quality Control

## Purpose
Ensure code quality, security, and consistency before every commit.

## Why This Skill Exists
Bugs caught early are 10x cheaper to fix. This checklist prevents common mistakes before they reach production.

## The 10-Point Checklist

### 1. ✅ Code Works
**Check:** Does the code actually run?

**Verify:**
- [ ] Code executes without errors
- [ ] Basic functionality tested
- [ ] No syntax errors
- [ ] No missing imports/dependencies

**Red Flags:**
- "Should work" without testing
- Missing error handling
- Untested edge cases

---

### 2. ✅ No Secrets or Keys
**Check:** Are API keys, passwords, or tokens exposed?

**Verify:**
- [ ] No hardcoded API keys
- [ ] No passwords in code
- [ ] No database credentials
- [ ] No private tokens

**Red Flags:**
```javascript
// BAD:
const API_KEY = "sk-1234567890abcdef"
const password = "mypassword123"
```

**Good Practice:**
```javascript
// GOOD:
const API_KEY = process.env.API_KEY
```

---

### 3. ✅ Follows Project Style
**Check:** Does code match existing patterns?

**Verify:**
- [ ] Same naming conventions
- [ ] Same formatting (indentation, quotes)
- [ ] Same architecture patterns
- [ ] Consistent file structure

**Red Flags:**
- Mixing camelCase and snake_case
- Different indentation in same file
- New patterns without reason

---

### 4. ✅ Error Handling
**Check:** Are errors handled gracefully?

**Verify:**
- [ ] Try-catch blocks where needed
- [ ] Error messages are clear
- [ ] Failures don't crash the app
- [ ] Edge cases considered

**Red Flags:**
```javascript
// BAD:
const data = JSON.parse(input) // Can crash

// GOOD:
try {
  const data = JSON.parse(input)
} catch (error) {
  console.error("Invalid JSON:", error)
  return null
}
```

---

### 5. ✅ Documentation
**Check:** Is code understandable?

**Verify:**
- [ ] Complex functions have comments
- [ ] README updated if needed
- [ ] Function names are descriptive
- [ ] Variable names make sense

**Red Flags:**
- Single-letter variable names (except loops)
- No comments on complex logic
- Cryptic function names

---

### 6. ✅ No Debug Code Left
**Check:** Cleaned up development code?

**Verify:**
- [ ] No console.log statements
- [ ] No debugger statements
- [ ] No TODO comments (or moved to issues)
- [ ] No commented-out code blocks

**Red Flags:**
```javascript
console.log("DEBUG: here")
console.log(data) // for debugging
// TODO: fix this later
debugger
```

---

### 7. ✅ Security Check
**Check:** Common vulnerabilities?

**Verify:**
- [ ] No SQL injection risks
- [ ] No XSS vulnerabilities
- [ ] Input validation present
- [ ] Output is escaped properly

**Red Flags:**
```javascript
// BAD - SQL Injection:
query = `SELECT * FROM users WHERE id = ${userId}`

// GOOD:
query = "SELECT * FROM users WHERE id = ?"
db.query(query, [userId])
```

---

### 8. ✅ Performance
**Check:** Any obvious performance issues?

**Verify:**
- [ ] No N+1 queries
- [ ] No infinite loops
- [ ] Efficient algorithms
- [ ] No unnecessary re-renders (React)

**Red Flags:**
- Nested loops without limits
- Database queries in loops
- Loading huge files into memory

---

### 9. ✅ Dependencies
**Check:** Are new dependencies justified?

**Verify:**
- [ ] New packages are necessary
- [ ] Package is maintained
- [ ] No duplicate functionality
- [ ] package.json updated

**Red Flags:**
- Adding library for one function
- Using outdated packages
- Multiple libraries for same thing

---

### 10. ✅ Git Hygiene
**Check:** Is commit clean?

**Verify:**
- [ ] Commit message is clear
- [ ] Only relevant files included
- [ ] No accidental file deletions
- [ ] Reasonable commit size

**Red Flags:**
- "fix stuff" commit messages
- 50 files changed at once
- Mixing features in one commit

---

## Review Process

### Before Committing:
```bash
1. Write code
2. Run checklist (mentally or with script)
3. Fix any issues
4. Test again
5. Commit with clear message
```

### Quick Review Script:
```bash
./review-check.sh
```

Output:
```
🔍 Code Review Checklist

[✓] 1. Code Works - PASS
[✓] 2. No Secrets - PASS
[!] 3. Style Check - WARNING: Mixed indentation
[✓] 4. Error Handling - PASS
[!] 5. Documentation - TODO: Add function comment
[✓] 6. No Debug Code - PASS
[✓] 7. Security - PASS
[✓] 8. Performance - PASS
[✓] 9. Dependencies - PASS
[✓] 10. Git Hygiene - PASS

⚠️  2 warnings - fix before commit?
```

## Severity Levels

### 🔴 BLOCKING (Must Fix)
- Secrets exposed
- Security vulnerabilities
- Code doesn't work
- Syntax errors

### 🟡 WARNING (Should Fix)
- Style inconsistencies
- Missing documentation
- Debug code left
- Performance issues

### 🟢 INFO (Nice to Have)
- Could add more comments
- Could optimize further
- Minor improvements

## Integration

### With Git
Add as pre-commit hook:
```bash
# .git/hooks/pre-commit
./review-check.sh || exit 1
```

### With Task Planner
Every development task includes review:
```
[ ] Task 3.5: Build API endpoint
    └── [ ] Code Review Checklist
```

### With Self-Review
Before saying "ready":
```
✅ Self-Review: Code Review Checklist passed
```

---
Last Updated: 2026-03-13
Status: Active
