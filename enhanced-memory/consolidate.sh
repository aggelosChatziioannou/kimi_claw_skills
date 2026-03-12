#!/bin/bash
# Enhanced Memory Consolidation - Daily Pattern Analysis
# Usage: ./consolidate.sh

echo "🧠 ENHANCED MEMORY CONSOLIDATION"
echo "================================"
echo ""
echo "📅 Date: $(date)"
echo ""

# Check for patterns in recent memory files
echo "🔍 Analyzing recent conversations..."

# Pattern 1: Timezone preference
if grep -r "Europe/Athens\|Ελλάδα\|Greece" /root/.openclaw/workspace/memory/ 2>/dev/null | grep -q .; then
  echo "✓ Pattern: Timezone = Europe/Athens (confirmed)"
fi

# Pattern 2: Name preference
if grep -r "Boss\|Αφεντικό" /root/.openclaw/workspace/memory/ 2>/dev/null | grep -q .; then
  echo "✓ Pattern: Preferred name = Boss (confirmed)"
fi

# Pattern 3: Git verification
if grep -r "verify\|verification\|fresh clone" /root/.openclaw/workspace/memory/ 2>/dev/null | grep -q .; then
  echo "✓ Pattern: Git verification required (confirmed)"
fi

# Pattern 4: Communication style
if grep -r "status updates\|continuous\|every 15" /root/.openclaw/workspace/memory/ 2>/dev/null | grep -q .; then
  echo "✓ Pattern: Continuous communication preferred (confirmed)"
fi

echo ""
echo "📝 Consolidation complete!"
echo "💡 Ready to apply learned patterns."
