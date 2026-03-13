#!/usr/bin/env python3
"""
AI Semantic Code Analyzer - Deep code understanding and analysis
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class IssueType(Enum):
    BUG = "bug"
    SECURITY = "security"
    PERFORMANCE = "performance"
    STYLE = "style"
    BEST_PRACTICE = "best_practice"

@dataclass
class Issue:
    type: IssueType
    severity: Severity
    line: int
    message: str
    fix: str
    explanation: str

@dataclass
class AnalysisResult:
    file_name: str
    language: str
    lines: int
    score: int
    issues: List[Issue]
    summary: str


class CodeAnalyzer:
    """AI-powered semantic code analyzer."""
    
    def __init__(self):
        self.security_patterns = self._load_security_patterns()
        self.performance_patterns = self._load_performance_patterns()
    
    def _load_security_patterns(self) -> Dict:
        """Load security vulnerability patterns."""
        return {
            "sql_injection": {
                "pattern": r'["\'].*\{.*\}.*["\']|f["\'].*\{.*\}',
                "message": "Potential SQL injection - user input in query",
                "severity": Severity.CRITICAL,
                "fix": "Use parameterized queries",
                "languages": ["python", "javascript", "java"]
            },
            "hardcoded_secret": {
                "pattern": r'(password|secret|key|token)\s*=\s*["\'][^"\']+["\']',
                "message": "Hardcoded credential detected",
                "severity": Severity.CRITICAL,
                "fix": "Use environment variables",
                "languages": ["*"]
            },
            "xss_vulnerability": {
                "pattern": r'innerHTML|dangerouslySetInnerHTML|\.html\(',
                "message": "Potential XSS vulnerability",
                "severity": Severity.HIGH,
                "fix": "Use textContent or sanitize input",
                "languages": ["javascript", "typescript"]
            },
            "insecure_random": {
                "pattern": r'Math\.random\(\)',
                "message": "Math.random() not cryptographically secure",
                "severity": Severity.MEDIUM,
                "fix": "Use crypto.getRandomValues() for security",
                "languages": ["javascript"]
            }
        }
    
    def _load_performance_patterns(self) -> Dict:
        """Load performance anti-patterns."""
        return {
            "nested_loop": {
                "pattern": r'for.*\n.*for',
                "message": "Nested loops detected - potential O(n²) complexity",
                "severity": Severity.MEDIUM,
                "fix": "Use HashMap/Set for O(1) lookups",
                "languages": ["*"]
            },
            "string_concat_loop": {
                "pattern": r'for.*\+.*=.*["\']',
                "message": "String concatenation in loop",
                "severity": Severity.LOW,
                "fix": "Use array join or StringBuilder",
                "languages": ["*"]
            }
        }
    
    def detect_language(self, code: str, file_name: str = "") -> str:
        """Detect programming language from code or filename."""
        if file_name:
            ext = Path(file_name).suffix.lower()
            lang_map = {
                ".js": "javascript",
                ".ts": "typescript",
                ".py": "python",
                ".java": "java",
                ".go": "go",
                ".rs": "rust",
                ".sql": "sql"
            }
            if ext in lang_map:
                return lang_map[ext]
        
        # Detect from code patterns
        if "def " in code and ":" in code:
            return "python"
        elif "function" in code or "const" in code or "let" in code:
            return "javascript"
        elif "public static" in code or "class" in code:
            return "java"
        
        return "unknown"
    
    def find_bugs(self, code: str, language: str) -> List[Issue]:
        """Find bugs in code."""
        issues = []
        lines = code.split('\n')
        
        # Common bug patterns
        bug_patterns = {
            "javascript": [
                {
                    "pattern": r'=\s*==?',
                    "message": "Assignment in condition (use === for comparison)",
                    "severity": Severity.HIGH
                },
                {
                    "pattern": r'\.then\([^)]*\)\s*\.',
                    "message": "Promise chain without catch - unhandled rejection",
                    "severity": Severity.MEDIUM
                },
                {
                    "pattern": r'undefined|null\s*\.',
                    "message": "Potential null/undefined access",
                    "severity": Severity.HIGH
                }
            ],
            "python": [
                {
                    "pattern": r'except\s*:\s*$',
                    "message": "Bare except clause - catches all exceptions including KeyboardInterrupt",
                    "severity": Severity.MEDIUM
                },
                {
                    "pattern": r'==\s*(True|False|None)',
                    "message": "Use 'is' for comparing with singletons",
                    "severity": Severity.LOW
                }
            ]
        }
        
        patterns = bug_patterns.get(language, [])
        
        for line_num, line in enumerate(lines, 1):
            for pattern in patterns:
                if re.search(pattern["pattern"], line):
                    issues.append(Issue(
                        type=IssueType.BUG,
                        severity=pattern["severity"],
                        line=line_num,
                        message=pattern["message"],
                        fix=f"Review line {line_num} and fix the issue",
                        explanation="Detected common bug pattern"
                    ))
        
        return issues
    
    def find_security_issues(self, code: str, language: str) -> List[Issue]:
        """Find security vulnerabilities."""
        issues = []
        lines = code.split('\n')
        
        for vuln_name, vuln_info in self.security_patterns.items():
            if vuln_info["languages"][0] != "*" and language not in vuln_info["languages"]:
                continue
            
            for line_num, line in enumerate(lines, 1):
                if re.search(vuln_info["pattern"], line, re.IGNORECASE):
                    issues.append(Issue(
                        type=IssueType.SECURITY,
                        severity=vuln_info["severity"],
                        line=line_num,
                        message=vuln_info["message"],
                        fix=vuln_info["fix"],
                        explanation=f"Security vulnerability: {vuln_name}"
                    ))
        
        return issues
    
    def find_performance_issues(self, code: str, language: str) -> List[Issue]:
        """Find performance issues."""
        issues = []
        lines = code.split('\n')
        
        for pattern_name, pattern_info in self.performance_patterns.items():
            # Simple line-by-line check
            for line_num, line in enumerate(lines, 1):
                if re.search(pattern_info["pattern"], line):
                    issues.append(Issue(
                        type=IssueType.PERFORMANCE,
                        severity=pattern_info["severity"],
                        line=line_num,
                        message=pattern_info["message"],
                        fix=pattern_info["fix"],
                        explanation="Performance anti-pattern detected"
                    ))
        
        # Detect O(n²) patterns (simplified)
        loop_count = sum(1 for line in lines if re.search(r'^\s*(for|while)\s+', line))
        if loop_count >= 2:
            # Check for nested loops (simplified detection)
            issues.append(Issue(
                type=IssueType.PERFORMANCE,
                severity=Severity.MEDIUM,
                line=1,
                message=f"Multiple loops detected ({loop_count}). Check for nested loops that could be O(n²)",
                fix="Consider using Set/Map for O(1) lookups",
                explanation="Nested loops can cause quadratic time complexity"
            ))
        
        return issues
    
    def calculate_score(self, issues: List[Issue], lines: int) -> int:
        """Calculate overall code quality score."""
        base_score = 100
        
        deductions = {
            Severity.CRITICAL: 25,
            Severity.HIGH: 15,
            Severity.MEDIUM: 8,
            Severity.LOW: 3
        }
        
        for issue in issues:
            base_score -= deductions.get(issue.severity, 5)
        
        # Normalize by lines of code
        if lines > 0:
            base_score = max(0, min(100, base_score))
        
        return base_score
    
    def analyze(self, code: str, file_name: str = "") -> AnalysisResult:
        """Perform comprehensive code analysis."""
        language = self.detect_language(code, file_name)
        lines = len(code.split('\n'))
        
        # Run all analyses
        bugs = self.find_bugs(code, language)
        security = self.find_security_issues(code, language)
        performance = self.find_performance_issues(code, language)
        
        all_issues = bugs + security + performance
        
        # Calculate score
        score = self.calculate_score(all_issues, lines)
        
        # Generate summary
        summary = self._generate_summary(all_issues, score)
        
        return AnalysisResult(
            file_name=file_name or "unnamed",
            language=language,
            lines=lines,
            score=score,
            issues=all_issues,
            summary=summary
        )
    
    def _generate_summary(self, issues: List[Issue], score: int) -> str:
        """Generate human-readable summary."""
        bug_count = sum(1 for i in issues if i.type == IssueType.BUG)
        security_count = sum(1 for i in issues if i.type == IssueType.SECURITY)
        perf_count = sum(1 for i in issues if i.type == IssueType.PERFORMANCE)
        
        critical = sum(1 for i in issues if i.severity == Severity.CRITICAL)
        high = sum(1 for i in issues if i.severity == Severity.HIGH)
        
        if score >= 90:
            quality = "Excellent"
        elif score >= 75:
            quality = "Good"
        elif score >= 60:
            quality = "Fair"
        else:
            quality = "Needs Improvement"
        
        return f"{quality} code quality. Found {bug_count} bugs, {security_count} security issues, {perf_count} performance issues. {critical} critical, {high} high severity."
    
    def format_report(self, result: AnalysisResult) -> str:
        """Format analysis result as readable report."""
        lines = [
            "🔍 CODE ANALYSIS REPORT",
            "",
            f"📊 OVERVIEW",
            f"• File: {result.file_name}",
            f"• Language: {result.language}",
            f"• Lines: {result.lines}",
            f"• Score: {result.score}/100",
            ""
        ]
        
        # Group issues by type
        bugs = [i for i in result.issues if i.type == IssueType.BUG]
        security = [i for i in result.issues if i.type == IssueType.SECURITY]
        performance = [i for i in result.issues if i.type == IssueType.PERFORMANCE]
        
        if bugs:
            lines.append(f"⚠️  BUGS ({len(bugs)}):")
            for issue in bugs:
                lines.append(f"   Line {issue.line}: {issue.message}")
                lines.append(f"   💡 Fix: {issue.fix}")
                lines.append("")
        
        if security:
            lines.append(f"🔒 SECURITY ISSUES ({len(security)}):")
            for issue in security:
                emoji = "🚨" if issue.severity == Severity.CRITICAL else "⚠️"
                lines.append(f"   {emoji} Line {issue.line} [{issue.severity.value.upper()}]: {issue.message}")
                lines.append(f"   💡 Fix: {issue.fix}")
                lines.append("")
        
        if performance:
            lines.append(f"⚡ PERFORMANCE ISSUES ({len(performance)}):")
            for issue in performance:
                lines.append(f"   Line {issue.line}: {issue.message}")
                lines.append(f"   💡 Fix: {issue.fix}")
                lines.append("")
        
        if not result.issues:
            lines.append("✅ No issues found! Great code!")
            lines.append("")
        
        lines.append(f"📝 SUMMARY: {result.summary}")
        
        return "\n".join(lines)


# Demo/test
if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    
    # Test code with various issues
    test_code = '''
def get_user(username):
    password = "admin123"  # Hardcoded secret
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return db.execute(query)

def process(items):
    result = []
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j]:
                result.append(items[i])
    return result

if user == True:  # Wrong comparison
    print("Admin")
'''
    
    print("=" * 60)
    print("AI CODE ANALYZER DEMO")
    print("=" * 60)
    print()
    
    result = analyzer.analyze(test_code, "test.py")
    print(analyzer.format_report(result))
    
    print()
    print("=" * 60)
    print("JSON OUTPUT:")
    print("=" * 60)
    print(json.dumps(asdict(result), indent=2, default=str))
