import time
import requests

async def handle_incoming_webhook(payload: dict):
    time.sleep(15)
    try:
        resp = requests.get("https://api.github.com/zen")
        return resp.text
    except Exception:
        # just die here.
        pass
