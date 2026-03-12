#!/bin/bash
# Know Thyself - Pre-Flight Verification
# Run BEFORE proposing any architecture to user

echo "=== Pre-Flight Capability Check ==="
echo ""

# Check for HTTP server requirement
if echo "$1" | grep -qi "http server\|webhook\|port\|localhost:18789"; then
    echo "❌ BLOCKED: HTTP server/webhook required"
    echo "   Kimi-Claw cannot open ports or receive HTTP requests"
    echo "   Alternative: Use polling or message-based triggers"
    exit 1
fi

# Check for 24/7 background requirement
if echo "$1" | grep -qi "24/7\|always on\|background\|persistent connection\|real-time"; then
    echo "⚠ WARNING: 24/7 operation requested"
    echo "   Kimi-Claw wakes only on user messages"
    echo "   Alternative: OpenClaw Gateway cron (if configured)"
    echo "   Or: User messages trigger to check status"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for local machine access
if echo "$1" | grep -qi "local file\|your computer\|ssh\|local device\|camera\|location"; then
    echo "❌ BLOCKED: Local machine access required"
    echo "   Kimi-Claw runs in cloud container"
    echo "   Alternative: Use OpenClaw for local device access"
    exit 1
fi

# Check for bidirectional real-time
if echo "$1" | grep -qi "bidirectional\|websocket\|socket.io\|live update\|push notification"; then
    echo "❌ BLOCKED: Bidirectional real-time communication"
    echo "   Kimi-Claw cannot maintain persistent connections"
    echo "   Alternative: Static generation or polling"
    exit 1
fi

echo "✓ PASSED: Solution appears compatible with Kimi-Claw capabilities"
echo ""
echo "✓ File operations available"
echo "✓ Git operations available"
echo "✓ Web search available"
echo "✓ Bash commands (container only)"
exit 0
