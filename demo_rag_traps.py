"""
demo_rag_traps.py

This file contains deliberate violations ("RAG Traps") of the engineering standards
defined in our ADK GitHub Agent RAG corpus (mock_docs/docs/*.md).

When you commit this file to a branch and open a Pull Request in gcp-scratch,
our Vertex AI Agent Engine PR Reviewer agent (`pr_reviewer`) will query the RAG Engine,
detect these specific violations, and post inline line comments using our exact
RAG severity header format (`[SEVERITY: CRITICAL / MODERATE / NITPICK]`).
"""

import time
import requests

# ==============================================================================
# TRAP 1: Blocking Asynchronous Call & Bare Except (Violation of python_style_guide.md)
# ==============================================================================
async def handle_incoming_webhook(payload: dict):
    """Processes incoming webhooks asynchronously."""
    # 🔴 CRITICAL VIOLATION: Synchronous time.sleep() inside async def blocks the event loop!
    time.sleep(5)
    
    try:
        # 🔴 CRITICAL VIOLATION: Synchronous requests.get inside async def without asyncio.to_thread!
        resp = requests.get("https://api.github.com/zen")
        return resp.text
    except Exception:
        # 🔴 CRITICAL VIOLATION: Bare except catching Exception without exc_info=True logging!
        pass


# ==============================================================================
# TRAP 2: Insecure Cryptographic Signature Comparison (Violation of python_style_guide.md)
# ==============================================================================
def verify_github_webhook(secret: str, received_signature: str, payload: bytes) -> bool:
    """Verifies incoming webhook signatures."""
    expected = "sha256=" + secret
    # 🔴 CRITICAL VIOLATION: Direct '==' string comparison instead of hmac.compare_digest (Timing Attack)!
    if expected == received_signature:
        return True
    return False


# ==============================================================================
# TRAP 3: Package Management Instructions (Violation of python_style_guide.md)
# ==============================================================================
# To install dependencies and run this standalone demo locally:
# virtualenv venv && source venv/bin/activate
# pip install requests pydantic
# 🟡 MODERATE VIOLATION: Using pip/virtualenv instead of our mandatory 'uv' package manager!
