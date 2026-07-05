#!/usr/bin/env bash
# demo_reset.sh
# Cleans up and resets local/remote test-rag-review branches after finishing a demo.

set -e

echo "=========================================================="
echo "  🧹 Resetting gcp-scratch repo after RAG Demo"
echo "=========================================================="

# 1. Switch back to default branch (dev or main)
git checkout dev 2>/dev/null || git checkout main

# 2. Delete local test-rag-review branch
git branch -D test-rag-review 2>/dev/null || true

# 3. Delete remote test-rag-review branch from GitHub
git push origin --delete test-rag-review 2>/dev/null || true

echo ""
echo "✅ Reset complete! Local and remote 'test-rag-review' branches deleted."
echo "   (Note: If your PR is still open on GitHub, simply click 'Close pull request' on the web UI)."
echo "=========================================================="
