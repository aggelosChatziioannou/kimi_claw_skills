# AI Semantic Code Analyzer

Deep code understanding with AI-powered analysis.

## What It Does

🔍 **Understands code behavior** - Not just pattern matching  
🐛 **Bug prediction** - Finds issues before runtime  
🔒 **Security scanning** - Detects vulnerabilities  
⚡ **Performance analysis** - Identifies bottlenecks  
🔄 **Multi-file refactoring** - Rename across codebase  

## Features

### 1. Semantic Code Understanding
- Analyzes what code actually does
- Context-aware suggestions
- Multi-file analysis

### 2. Bug Detection
- Undefined variables
- Logic errors
- Type mismatches
- Race conditions

### 3. Security Scanning
- SQL injection
- XSS vulnerabilities
- Hardcoded secrets
- Insecure dependencies

### 4. Performance Analysis
- Time complexity detection
- Memory leaks
- Inefficient algorithms
- Optimization suggestions

### 5. Auto-Fixes
- One-click bug fixes
- Security patches
- Performance improvements
- Refactoring suggestions

## How It Works

```
You: Send code
↓
Analyzer: Parses and understands semantics
↓
Detects: Bugs, security, performance issues
↓
Report: Detailed analysis with fixes
↓
You: Apply fixes (optional)
```

## Usage

### Analyze Code
```
"Analyze this code: [paste code]"
"Review my function for bugs"
"Check this for security issues"
```

### Multi-File Analysis
```
"Analyze src/components/ directory"
"Find all usages of 'userData' variable"
"Rename 'oldFunction' to 'newFunction' across files"
```

## Example Output

```
🔍 CODE ANALYSIS REPORT

File: src/auth.js
Lines: 45-67

⚠️ BUGS (2):
• Line 23: Variable 'userData' may be undefined
  Fix: Add null check before accessing
  
• Line 45: Missing await on async function
  Fix: Add 'await' keyword

🔒 SECURITY (1):
• Line 67: Potential SQL injection
  Risk: HIGH
  Fix: Use parameterized queries

⚡ PERFORMANCE (1):
• Line 89: O(n²) loop detected
  Current: Nested loops over array
  Suggestion: Use HashMap for O(n)

📊 OVERALL SCORE: 72/100

💡 RECOMMENDED ACTIONS:
1. Fix SQL injection (HIGH priority)
2. Add null checks
3. Optimize nested loop
```

## Supported Languages

- JavaScript/TypeScript
- Python
- Java
- Go
- Rust
- SQL

## Files

- `SKILL.md` - Documentation
- `code_analyzer.py` - Core implementation
- `security_patterns.json` - Security rules
- `performance_rules.json` - Performance patterns

## Version

1.0.0 (2026-03-13)
