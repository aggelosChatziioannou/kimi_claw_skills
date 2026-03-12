#!/bin/bash
# Query Classifier - Auto-detect query type and set strategy

QUERY="$1"

# Check for COMPLEX indicators
if echo "$QUERY" | grep -qi "φτιάξε\|κάνε\|δημιούργησε\|ανάλυσε\|έρευνα\|φτιάξ\|build\|create\|analyze\|research"; then
    echo "COMPLEX"
    exit 0
fi

# Check for MEDIUM indicators  
if echo "$QUERY" | grep -qi "σύγκρινε\|εξήγησε\|βρες\|compare\|explain\|find\|search"; then
    echo "MEDIUM"
    exit 0
fi

# Check query length (rough heuristic)
WORDS=$(echo "$QUERY" | wc -w)
if [ "$WORDS" -gt 15 ]; then
    echo "MEDIUM"
    exit 0
fi

# Default to SIMPLE
echo "SIMPLE"
