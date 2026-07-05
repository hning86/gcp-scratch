#!/usr/bin/env bash
# demo_start.sh
# Quickly creates the test-rag-review branch, commits demo_rag_traps.py, and pushes to GitHub.

set -e

echo "=========================================================="
echo "  🚀 Starting ADK RAG Grounding Demo for gcp-scratch"
echo "=========================================================="

# 1. Switch to default branch (dev or main)
git checkout dev 2>/dev/null || git checkout main

# 2. Clean up any leftover local demo branch from a previous run
git branch -D test-rag-review 2>/dev/null || true

# 3. Create fresh demo branch
git checkout -b test-rag-review

# 4. Stage our RAG Traps demo file
git add demo_rag_traps.py

# 5. Commit with an obvious test message
git commit -m "test: add demo RAG traps (async blocking, == sig check, pip)"

# 6. Push to GitHub origin (overwrite remote if leftover)
git push -u origin test-rag-review --force

echo ""
echo "✅ Demo branch 'test-rag-review' successfully pushed to GitHub!"
echo ""
echo "👉 Next step: Open this URL in Chrome to create your Pull Request:"
echo "   https://github.com/hning86/gcp-scratch/pull/new/test-rag-review"
echo "=========================================================="
