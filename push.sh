#!/usr/bin/env bash
set -e

# Check if a commit message was provided as an argument
if [ -z "$1" ]; then
  echo "Error: No commit message provided."
  echo "Usage: $0 \"Your commit message\""
  exit 1
fi

COMMIT_MSG="$1"

echo "Adding all changes..."
git add -A

echo "Committing changes with message: \"$COMMIT_MSG\"..."
git commit -m "$COMMIT_MSG"

echo "Pushing changes..."
git push

echo "Successfully committed and pushed!"
