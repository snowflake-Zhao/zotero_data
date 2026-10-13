#!/bin/bash

# Script to find and commit newly added files in Zotero storage
# Usage: ./commit-storage.sh

cd "D:/Zotero/zotero_data" || exit 1

echo "=== Finding untracked files in storage directory ==="

# Find all PDF and data files, excluding .zotero-* cache/state directories
git ls-files --others --exclude-standard storage/ | grep -v '\.zotero-ft-cache' | grep -v '\.zotero-reader-state' > /tmp/new_files.txt

if [ ! -s /tmp/new_files.txt ]; then
    echo "No new files found in storage directory."
    exit 0
fi

echo ""
echo "Newly added files:"

# Add all untracked files to staging at once (handles special characters properly)
git add --pathspec-from-file=/tmp/new_files.txt

echo ""
echo "Files staged for commit."
echo ""

# Create commit with timestamped message
COMMIT_MSG="commit-storage: add newly updated files $(date '+%Y-%m-%d %H:%M')"
echo "Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo ""
echo "=== Commit complete ==="
