#!/usr/bin/env python3
"""
Code Reviewer - AI-powered code analysis
"""

import re
import ast
from pathlib import Path

class CodeReviewer:
    def __init__(self):
        self.issues = {
            "bugs": [],
            "security": [],
            "performance": [],
            "style": [],
            "suggestions": []
        }
    
    def review_file(self, filepath, content):
        """Review a single file."""
        self.issues = {k: [] for k in self.issues}
        
        # Check for common issues
        self._check_undefined_vars(content)
        self._check_hardcoded_secrets(content)
        self._check_sql_injection(content)
        self._check_console_logs(content)
        self._check_todo_fixme(content)
        self._check_long_functions(content)
        self._check_empty_catch(content)
        
        return self._generate_report(filepath)
    
    def _check_undefined_vars(self, content):
        """Check for potentially undefined variables."""
        # Simple pattern matching for common cases
        patterns = [
            (r'\buser\b.*\?', "Variable 'user' may be undefined"),
            (r'\bdata\b.*\?', "Variable 'data' may be undefined"),
            (r'if\s*\(\s*\w+\s*\)', "Check if variable exists before use"),
        ]
        for pattern, msg in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.issues["bugs"].append(msg)
    
    def _check_hardcoded_secrets(self, content):
        """Check for hardcoded secrets."""
        secret_patterns = [
            r'(password|passwd|pwd)\s*[=:]\s*["\'][^"\']+["\']',
            r'(api_key|apikey|token)\s*[=:]\s*["\'][^"\']+["\']',
            r'(secret|private_key)\s*[=:]\s*["\'][^"\']+["\']',
        ]
        for pattern in secret_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.issues["security"].append("Potential hardcoded secret detected")
    
    def _check_sql_injection(self, content):
        """Check for SQL injection risks."""
        sql_patterns = [
            r'execute\s*\(\s*["\'].*\+.*["\']',
            r'query\s*\(\s*["\'].*\$.*["\']',
            r'SELECT.*FROM.*\+',
        ]
        for pattern in sql_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.issues["security"].append("Potential SQL injection risk")
    
    def _check_console_logs(self, content):
        """Check for console.log statements."""
        if re.search(r'console\.(log|warn|error)\s*\(', content):
            self.issues["style"].append("Remove console.log statements before production")
    
    def _check_todo_fixme(self, content):
        """Check for TODO/FIXME comments."""
        todos = re.findall(r'(TODO|FIXME|XXX|HACK).*', content, re.IGNORECASE)
        for todo in todos:
            self.issues["suggestions"].append(f"Address {todo}")
    
    def _check_long_functions(self, content):
        """Check for long functions."""
        lines = content.split('\n')
        in_function = False
        func_start = 0
        brace_count = 0
        
        for i, line in enumerate(lines):
            if re.match(r'\s*(function|const|let|var)\s+\w+\s*[=\(]', line):
                in_function = True
                func_start = i
                brace_count = line.count('{') - line.count('}')
            elif in_function:
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0:
                    func_length = i - func_start
                    if func_length > 30:
                        self.issues["style"].append(f"Function too long ({func_length} lines)")
                    in_function = False
    
    def _check_empty_catch(self, content):
        """Check for empty catch blocks."""
        if re.search(r'catch\s*\(\s*\w+\s*\)\s*\{\s*\}', content):
            self.issues["bugs"].append("Empty catch block - handle the error")
    
    def _calculate_score(self):
        """Calculate code quality score."""
        total_issues = sum(len(v) for v in self.issues.values())
        if total_issues == 0:
            return 10
        elif total_issues <= 2:
            return 8
        elif total_issues <= 5:
            return 6
        else:
            return max(3, 10 - total_issues)
    
    def _generate_report(self, filepath):
        """Generate review report."""
        score = self._calculate_score()
        
        report = f"""═══════════════════════════════════════════════════
🔍 CODE REVIEW REPORT
═══════════════════════════════════════════════════

📁 File: {filepath}

"""
        
        # Bugs
        if self.issues["bugs"]:
            report += f"🐛 BUGS ({len(self.issues['bugs'])}):\n"
            for issue in self.issues["bugs"]:
                report += f"   ❌ {issue}\n"
            report += "\n"
        
        # Security
        if self.issues["security"]:
            report += f"🔒 SECURITY ({len(self.issues['security'])}):\n"
            for issue in self.issues["security"]:
                report += f"   ⚠️  {issue}\n"
            report += "\n"
        
        # Performance
        if self.issues["performance"]:
            report += f"⚡ PERFORMANCE ({len(self.issues['performance'])}):\n"
            for issue in self.issues["performance"]:
                report += f"   💡 {issue}\n"
            report += "\n"
        
        # Style
        if self.issues["style"]:
            report += f"📐 STYLE ({len(self.issues['style'])}):\n"
            for issue in self.issues["style"]:
                report += f"   ✏️  {issue}\n"
            report += "\n"
        
        # Suggestions
        if self.issues["suggestions"]:
            report += f"📝 SUGGESTIONS:\n"
            for issue in self.issues["suggestions"]:
                report += f"   • {issue}\n"
            report += "\n"
        
        if not any(self.issues.values()):
            report += "✅ No issues found! Code looks good.\n\n"
        
        report += f"📊 SCORE: {score}/10\n"
        report += "\n═══════════════════════════════════════════════════"
        
        return report

def review_code(filepath):
    """Main entry point for code review."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        reviewer = CodeReviewer()
        return reviewer.review_file(filepath, content)
    except Exception as e:
        return f"Error reviewing file: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(review_code(sys.argv[1]))
    else:
        print("Usage: python code_reviewer.py <filepath>")
