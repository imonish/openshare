import os
import requests


def send_discord_alert(message: str):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        return  # fail silently if not configured

    payload = {
        "content": f"🚨 OpenShare Alert 🚨\n{message}"
    }

    try:
        requests.post(webhook_url, json=payload, timeout=5)
    except requests.RequestException:
        pass  # do not crash the app
