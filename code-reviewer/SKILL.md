# Code Reviewer

**ID:** code-reviewer  
**Version:** 1.0.0  
**Author:** Kimi-Claw  
**Compatibility:** OpenClaw, Git repositories

---

## Purpose

AI-powered code review assistant that analyzes code before commits, finds bugs, suggests improvements, and enforces best practices.

---

## What It Does

### 1. **Pre-Commit Analysis**
- Reviews code before git commit
- Checks for common bugs
- Identifies security issues
- Suggests optimizations

### 2. **Quality Checks**
- Code style compliance
- Best practices enforcement
- Performance bottlenecks
- Maintainability score

### 3. **Security Scan**
- Vulnerability detection
- Hardcoded secrets check
- Injection risk analysis
- Dependency vulnerabilities

### 4. **Smart Suggestions**
- Better implementations
- Refactoring ideas
- Documentation gaps
- Test coverage analysis

---

## Commands

### Before Commit
```
"Review this code before I commit"
"Check my changes"
"Code review on [file/path]"
"Should I commit this?"
```

### Specific Checks
```
"Security review on this code"
"Check for bugs in [file]"
"Performance review"
"Style check"
```

### Post-Review
```
"Generate review report"
"What are the critical issues?"
"Show me improvements"
```

---

## Review Categories

### 🐛 **Bugs & Logic Errors**
- Undefined variables
- Logic mistakes
- Null pointer risks
- Infinite loops

### 🔒 **Security Issues**
- SQL injection
- XSS vulnerabilities
- Hardcoded credentials
- Unsafe inputs

### ⚡ **Performance**
- Inefficient loops
- Memory leaks
- N+1 queries
- Unnecessary re-renders

### 📐 **Code Quality**
- Code smells
- Duplicate code
- Complexity issues
- Naming conventions

### 📝 **Best Practices**
- Missing error handling
- No input validation
- Poor documentation
- Test coverage gaps

---

## Output Format

```
═══════════════════════════════════════════════════
🔍 CODE REVIEW REPORT
═══════════════════════════════════════════════════

📁 File: src/components/Button.tsx

🐛 BUGS (2):
   ❌ Line 15: Variable 'user' may be undefined
   ❌ Line 42: Missing return statement

🔒 SECURITY (1):
   ⚠️  Line 28: User input not sanitized

⚡ PERFORMANCE (1):
   💡 Line 55: Use useMemo for expensive calculation

📐 STYLE (2):
   ✏️  Line 10: Function too long (>50 lines)
   ✏️  Line 33: Inconsistent naming

📝 SUGGESTIONS:
   • Add error boundary
   • Write unit tests
   • Document props interface

📊 SCORE: 7/10

═══════════════════════════════════════════════════
```

---

## Integration

- **Git Pre-Commit:** Auto-review before commits
- **GitHub:** Review PRs
- **VS Code:** Inline suggestions
- **CI/CD:** Automated checks

---

## Version History

- **1.0.0** (2026-03-13) - Initial release
  - Bug detection
  - Security scanning
  - Performance analysis
  - Quality scoring
