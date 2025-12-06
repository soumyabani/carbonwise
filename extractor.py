import requests
import os

CLOUDFLARE_URL = "https://api.cloudflare.com/client/v4/accounts/a761eb90bc3234b483b3a10a698b20ab/ai/run/@cf/meta/llama-3.1-8b-instruct"
API_KEY = os.getenv("CLOUDFLARE_API_KEY")

def extract_fields(text):
    prompt = f"""
Extract key data from this utility bill or receipt.
Return JSON strictly with:
- electricity_kwh
- amount
- store_name
- item_count
- date
- distance_km (if available)
Text:
{text}
"""

    response = requests.post(
        CLOUDFLARE_URL,
        json={"prompt": prompt},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )

    return response.json()["result"]["response"]

