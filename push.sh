#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status (error handling)
set -e

# Ensure that the user passed at least one argument for the commit message
if [ -z "$1" ]; then
  echo "Error: No commit message provided."
  echo "Usage: $0 \"Your commit message\""
  exit 1
fi

# Store the first argument passed to the script as the commit message
COMMIT_MSG="$1"

# Stage all modified, deleted, and untracked files across the entire working tree
echo "Adding all changes..."
git add -A

# Create a new commit with the staged changes using the provided message
echo "Committing changes with message: \"$COMMIT_MSG\"..."
git commit -m "$COMMIT_MSG"

# Push the committed changes to the configured upstream remote repository and branch
echo "Pushing changes..."
git push

# Notify the user upon successful execution
echo "Successfully committed and pushed!"

