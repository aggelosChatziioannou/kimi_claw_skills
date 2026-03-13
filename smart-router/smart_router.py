#!/usr/bin/env python3
"""
Smart Skill Router - Automatic skill activation based on context
"""

import json
import re
from pathlib import Path
from datetime import datetime

# Configuration
MEMORY_FILE = Path("/root/.openclaw/workspace/memory/smart-router.json")

# Default activation rules
DEFAULT_RULES = {
    "code_reviewer": {
        "patterns": [
            r"```[\w\s]*\n.*```",  # Code blocks
            r"function\s+\w+",     # Function definitions
            r"const\s+\w+\s*[=:]", # Variable declarations
            r"review.*code",        # Explicit requests
            r"bug.*fix",           # Bug mentions
            r"class\s+\w+",        # Class definitions
        ],
        "keywords": ["code", "function", "bug", "error", "syntax", "review"],
        "confidence": 0.9,
        "auto_activate": True
    },
    "second_brain": {
        "patterns": [
            r"remember.*",          # Remember requests
            r"capture.*",           # Capture requests
            r"idea.*",              # Ideas
            r"note.*",              # Notes
            r"what if.*",           # Hypotheticals
            r"brain dump.*",        # Brain dumps
        ],
        "keywords": ["remember", "idea", "note", "capture", "thought", "concept"],
        "confidence": 0.85,
        "auto_activate": True
    },
    "github_pro_sync": {
        "patterns": [
            r"git\s+(push|commit|clone)",  # Git commands
            r"github.*",                    # GitHub mentions
            r"deploy.*",                    # Deploy mentions
            r"pull request.*",              # PR mentions
        ],
        "keywords": ["git", "github", "push", "commit", "deploy", "merge"],
        "confidence": 0.92,
        "auto_activate": True
    },
    "deep_research": {
        "patterns": [
            r"research.*",           # Research requests
            r"find.*information",    # Info finding
            r"what is.*",           # Definition questions
            r"how does.*work",      # Explanation questions
            r"latest.*news",        # News requests
        ],
        "keywords": ["research", "find", "search", "information", "latest", "news"],
        "confidence": 0.8,
        "auto_activate": False  # Ask first
    },
    "task_planner": {
        "patterns": [
            r"plan.*project",        # Planning requests
            r"break down.*",         # Break down requests
            r"how to.*step",         # Step-by-step
            r"complex.*task",        # Complex tasks
        ],
        "keywords": ["plan", "break down", "steps", "roadmap", "complex"],
        "confidence": 0.75,
        "auto_activate": False
    }
}

class SmartRouter:
    def __init__(self):
        self.rules = self._load_rules()
        self.history = self._load_history()
    
    def _load_rules(self):
        """Load activation rules from memory or use defaults."""
        if MEMORY_FILE.exists():
            with open(MEMORY_FILE, 'r') as f:
                data = json.load(f)
                return data.get("rules", DEFAULT_RULES)
        return DEFAULT_RULES
    
    def _load_history(self):
        """Load activation history."""
        if MEMORY_FILE.exists():
            with open(MEMORY_FILE, 'r') as f:
                data = json.load(f)
                return data.get("history", [])
        return []
    
    def _save_memory(self):
        """Save rules and history to memory."""
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_FILE, 'w') as f:
            json.dump({
                "rules": self.rules,
                "history": self.history[-100:]  # Keep last 100
            }, f, indent=2)
    
    def analyze_input(self, user_input):
        """Analyze user input and return matching skills with confidence."""
        matches = []
        input_lower = user_input.lower()
        
        for skill_name, config in self.rules.items():
            confidence = 0.0
            matched_patterns = []
            
            # Check regex patterns
            for pattern in config.get("patterns", []):
                if re.search(pattern, user_input, re.IGNORECASE):
                    confidence += 0.3
                    matched_patterns.append(pattern)
            
            # Check keywords
            for keyword in config.get("keywords", []):
                if keyword.lower() in input_lower:
                    confidence += 0.2
            
            # Check explicit mentions
            if skill_name.replace("_", " ") in input_lower:
                confidence += 0.5
            
            # Cap at 1.0
            confidence = min(confidence, 1.0)
            
            # Check if meets minimum threshold
            if confidence >= config.get("confidence", 0.7):
                matches.append({
                    "skill": skill_name,
                    "confidence": confidence,
                    "auto_activate": config.get("auto_activate", False),
                    "matched_patterns": matched_patterns
                })
        
        # Sort by confidence
        matches.sort(key=lambda x: x["confidence"], reverse=True)
        
        return matches
    
    def should_activate(self, user_input):
        """Determine if and which skill should be activated."""
        matches = self.analyze_input(user_input)
        
        if not matches:
            return None
        
        top_match = matches[0]
        
        # Log activation
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": user_input[:100],
            "activated_skill": top_match["skill"],
            "confidence": top_match["confidence"],
            "auto": top_match["auto_activate"]
        })
        self._save_memory()
        
        return top_match
    
    def get_activation_message(self, match):
        """Generate activation message based on confidence."""
        skill_name = match["skill"]
        confidence = match["confidence"]
        
        skill_emoji = {
            "code_reviewer": "🔍",
            "second_brain": "🧠",
            "github_pro_sync": "🔐",
            "deep_research": "🔍",
            "task_planner": "📋"
        }
        
        emoji = skill_emoji.get(skill_name, "⚙️")
        
        if confidence >= 0.9:
            return f"{emoji} Auto-activating {skill_name.replace('_', ' ').title()}..."
        elif confidence >= 0.7:
            return f"{emoji} Using {skill_name.replace('_', ' ').title()} for this..."
        else:
            return f"{emoji} Should I use {skill_name.replace('_', ' ').title()}? (confidence: {confidence:.0%})"
    
    def learn_from_feedback(self, skill_name, was_helpful):
        """Learn from user feedback about activations."""
        if skill_name in self.rules:
            current_conf = self.rules[skill_name].get("confidence", 0.7)
            
            if was_helpful:
                # Increase confidence slightly
                self.rules[skill_name]["confidence"] = min(current_conf + 0.02, 1.0)
            else:
                # Decrease confidence
                self.rules[skill_name]["confidence"] = max(current_conf - 0.05, 0.5)
                # Maybe disable auto-activate
                if current_conf < 0.6:
                    self.rules[skill_name]["auto_activate"] = False
            
            self._save_memory()

def test_router():
    """Test the smart router."""
    router = SmartRouter()
    
    test_inputs = [
        "Here's my code: function test() { return 1; }",
        "Remember this idea I had",
        "Push this to GitHub",
        "git commit -m 'test'",
        "What if we created an app?",
        "Research the latest AI tools",
        "Plan my project",
    ]
    
    for user_input in test_inputs:
        match = router.should_activate(user_input)
        if match:
            msg = router.get_activation_message(match)
            print(f"\nInput: {user_input[:50]}...")
            print(f"→ {msg}")
            print(f"  Confidence: {match['confidence']:.0%}")
            print(f"  Auto-activate: {match['auto_activate']}")

if __name__ == "__main__":
    test_router()
