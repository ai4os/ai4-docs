"""
Make sure the documentation assistant agent that is mentioned all along the docs does
indeed exists (it may have changed IDs).
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import requests

# Load agent ID from documentation configuration
sys.path.insert(0, str(Path(__file__).parent / "source"))
from source.conf import ai_agent_id as AGENT_ID

load_dotenv()

BASE_URL = os.getenv("LITELLM_BASE_URL", "https://vllm.cloud.ai4eosc.eu")
API_KEY = os.getenv("LITELLM_API_KEY")

endpoint_url = f"{BASE_URL.rstrip('/')}/v1/agents/{AGENT_ID}"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
response = requests.get(endpoint_url, headers=headers)

if response.status_code in (200, 201):
    print("✅ Successfully retrieved documentation agent!")
    print(response.json())
else:
    print(f"❌ Failed to retrieve documentation agent: {response.status_code} - {response.text}")
    response.raise_for_status()