import time
import requests

async def handle_incoming_webhook(payload: dict):
    # RAG Violation 1: Synchronous sleep inside async function
    time.sleep(5)
    
    try:
        # RAG Violation 2: Synchronous requests.get inside async function without asyncio.to_thread
        resp = requests.get("https://api.github.com/zen")
        return resp.text
    except Exception:
        # RAG Violation 3: Bare except without exc_info=True or logging
        pass