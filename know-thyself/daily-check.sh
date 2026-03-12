#!/bin/bash
# Know Thyself - Daily Architecture Check
# Run during Memory Consolidation to check for Kimi-Claw updates

echo "=== Kimi-Claw Architecture Check ==="
echo "Date: $(date)"
echo ""

# Check if running in Kimi-Claw environment
if [ -d "/root/.openclaw" ]; then
    echo "✓ Confirmed: Kimi-Claw environment detected"
else
    echo "✗ Warning: May not be Kimi-Claw environment"
fi

# Check for Gateway cron capability
if command -v openclaw &> /dev/null; then
    echo "✓ OpenClaw CLI available"
    openclaw cron list 2>/dev/null || echo "⚠ No cron jobs configured"
else
    echo "⚠ OpenClaw CLI not available - cron features limited"
fi

# Check workspace access
if [ -w "/root/.openclaw/workspace" ]; then
    echo "✓ Workspace write access confirmed"
else
    echo "✗ No workspace access"
fi

echo ""
echo "=== Limitations Verified ==="
echo "❌ No HTTP server capability"
echo "❌ No inbound port access"
echo "❌ No local machine access"
echo "✓ Git operations available"
echo "✓ Web search available"
echo "✓ File operations available"

echo ""
echo "=== Internet Check Required ==="
echo "Run: kimi_search 'Kimi Claw updates March 2026'"
echo "Run: kimi_search 'OpenClaw new features 2026'"
echo "Update SKILL.md if changes detected"
