#!/bin/bash
# Code Review Checklist - Quick Check Script
# Usage: ./review-check.sh [file]

FILE="${1:-.}"

echo "🔍 CODE REVIEW CHECKLIST"
echo "========================"
echo ""

PASS=0
WARN=0
FAIL=0

# Check 1: Basic syntax (for JS/TS files)
if find "$FILE" -name "*.js" -o -name "*.ts" -o -name "*.tsx" 2>/dev/null | head -1 | grep -q .; then
  if command -v node >/dev/null 2>&1; then
    if node --check "$FILE" 2>/dev/null; then
      echo "[✓] 1. Code Works - PASS"
      ((PASS++))
    else
      echo "[✗] 1. Code Works - FAIL: Syntax error detected"
      ((FAIL++))
    fi
  else
    echo "[?] 1. Code Works - SKIP: Node not available"
  fi
else
  echo "[✓] 1. Code Works - SKIP: No JS/TS files"
fi

# Check 2: Secrets/Keys
if grep -rE "(api_key|apikey|password|secret|token)\\s*[=:]\\s*[\"'][^\"']{10,}" "$FILE" 2>/dev/null | grep -v "process.env\|env\." | head -1 | grep -q .; then
  echo "[✗] 2. No Secrets - FAIL: Potential secrets found"
  grep -rE "(api_key|apikey|password|secret|token)\\s*[=:]\\s*[\"'][^\"']{10,}" "$FILE" 2>/dev/null | grep -v "process.env\|env\." | head -3
  ((FAIL++))
else
  echo "[✓] 2. No Secrets - PASS"
  ((PASS++))
fi

# Check 3: Debug code (console.log)
if grep -r "console.log" "$FILE" 2>/dev/null | grep -v "node_modules" | head -1 | grep -q .; then
  echo "[!] 3. No Debug Code - WARNING: console.log found"
  grep -r "console.log" "$FILE" 2>/dev/null | grep -v "node_modules" | head -3
  ((WARN++))
else
  echo "[✓] 3. No Debug Code - PASS"
  ((PASS++))
fi

# Check 4: TODO comments
if grep -r "TODO\|FIXME\|XXX" "$FILE" 2>/dev/null | grep -v "node_modules" | head -1 | grep -q .; then
  echo "[!] 4. TODOs - INFO: TODO comments found"
  grep -r "TODO\|FIXME\|XXX" "$FILE" 2>/dev/null | grep -v "node_modules" | head -3
  ((WARN++))
else
  echo "[✓] 4. TODOs - PASS"
  ((PASS++))
fi

# Check 5: Mixed indentation (spaces vs tabs)
if find "$FILE" -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.json" 2>/dev/null | head -1 | xargs cat 2>/dev/null | grep -q $'\t'; then
  if find "$FILE" -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.json" 2>/dev/null | head -1 | xargs cat 2>/dev/null | grep -q "^  "; then
    echo "[!] 5. Style Check - WARNING: Mixed tabs and spaces"
    ((WARN++))
  else
    echo "[✓] 5. Style Check - PASS (using tabs)"
    ((PASS++))
  fi
else
  echo "[✓] 5. Style Check - PASS (using spaces)"
  ((PASS++))
fi

# Check 6: Large files (performance)
LARGE_FILES=$(find "$FILE" -type f -size +100k 2>/dev/null | grep -v "node_modules\|.git" | head -5)
if [ -n "$LARGE_FILES" ]; then
  echo "[!] 6. File Size - WARNING: Large files detected"
  echo "$LARGE_FILES"
  ((WARN++))
else
  echo "[✓] 6. File Size - PASS"
  ((PASS++))
fi

echo ""
echo "========================"
echo "Results: $PASS passed, $WARN warnings, $FAIL failures"
echo ""

if [ $FAIL -gt 0 ]; then
  echo "🔴 BLOCKING ISSUES - Fix before commit!"
  exit 1
elif [ $WARN -gt 0 ]; then
  echo "🟡 WARNINGS - Consider fixing"
  exit 0
else
  echo "🟢 ALL CHECKS PASSED - Ready to commit!"
  exit 0
fi
