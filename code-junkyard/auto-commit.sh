#!/bin/bash

# Auto-commit and push script
cd "/Users/ammarh/Library/Mobile Documents/iCloud~md~obsidian/Documents/tech/code-junkyard"

# Check if there are any changes
if [[ -n $(git status -s) ]]; then
    # Get current date and time
    timestamp=$(date "+%Y-%m-%d-%A-%H:%M:%S")

    # Add all changes
    git add -A

    # Commit with timestamp
    git commit -m "$timestamp - ab"

    # Push to remote
    git push

    echo "[$timestamp] Changes committed and pushed successfully"
else
    echo "[$(date "+%Y-%m-%d-%A-%H:%M:%S")] No changes to commit"
fi
