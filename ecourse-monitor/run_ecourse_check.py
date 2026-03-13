#!/usr/bin/env python3
"""
Ecourse Monitor Wrapper - Run through OpenClaw
Usage: python3 run_ecourse_check.py
"""

import sys
import json
from pathlib import Path

# Add skill to path
sys.path.insert(0, '/root/.openclaw/skills/ecourse-monitor')

from ecourse_monitor import run_check, format_morning_briefing, get_summary

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Ecourse Monitor')
    parser.add_argument('--briefing', action='store_true', help='Generate morning briefing')
    parser.add_argument('--summary', action='store_true', help='Get summary only')
    
    args = parser.parse_args()
    
    if args.briefing:
        # Generate morning briefing text
        print(format_morning_briefing())
    elif args.summary:
        # Get summary
        summary = get_summary()
        print(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
    else:
        # Run full check
        print("Running ecourse check...")
        # Note: Browser context would be passed from OpenClaw
        # For now, just output the morning briefing
        print(format_morning_briefing())

if __name__ == "__main__":
    main()
