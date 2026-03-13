# Code Reviewer

AI-powered code review before commits.

## What It Does

🔍 **Analyzes code** and finds:
- 🐛 Bugs & logic errors
- 🔒 Security vulnerabilities  
- ⚡ Performance issues
- 📐 Style problems
- 💡 Improvement suggestions

## Usage

### Review Before Commit
```
"Review this code"
"Check my changes"
"Should I commit this?"
```

### Specific Checks
```
"Security review"
"Performance check"
"Style analysis"
```

## Review Categories

| Category | Checks For |
|----------|-----------|
| Bugs | Undefined vars, logic errors, empty catch |
| Security | Hardcoded secrets, SQL injection, XSS |
| Performance | Inefficient code, memory leaks |
| Style | Long functions, console.logs, naming |

## Output

```
═══════════════════════════════════════════════════
🔍 CODE REVIEW REPORT
═══════════════════════════════════════════════════

📁 File: src/components/Button.tsx

🐛 BUGS (2):
   ❌ Variable 'user' may be undefined
   ❌ Missing return statement

🔒 SECURITY (1):
   ⚠️  Potential SQL injection risk

📊 SCORE: 7/10
```

## Files

- `SKILL.md` - Documentation
- `code_reviewer.py` - Implementation

## Version

1.0.0 (2026-03-13)
