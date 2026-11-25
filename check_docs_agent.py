"""
Make sure the documentation assistant agent that is mentioned all along the docs does
indeed exists (it may have changed IDs). If IDs have changed, try to find and replace
the new deployed agent.
"""

import os
import re
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

FALLBACK_AGENT_NAME = "documentation-assistant"
CONF_PATH = Path(__file__).parent / "source" / "conf.py"

base = BASE_URL.rstrip("/")
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
response = requests.get(f"{base}/v1/agents/{AGENT_ID}", headers=headers)

if response.status_code in (200, 201):
    print("✅ Successfully retrieved documentation agent!")
    sys.exit(0)

print(
    f"❌ Failed to retrieve documentation agent: {response.status_code} - {response.text}\n"
    f"Looking for an agent named '{FALLBACK_AGENT_NAME}' instead..."
)

list_response = requests.get(f"{base}/v1/agents", headers=headers)
list_response.raise_for_status()
agents = list_response.json()
if isinstance(agents, dict):
    agents = agents.get("agents") or agents.get("data") or []

new_id = next(
    (a.get("agent_id") for a in agents if a.get("agent_name") == FALLBACK_AGENT_NAME),
    None,
)
if not new_id:
    print(
        f"❌ No agent named '{FALLBACK_AGENT_NAME}' was found.\n"
        "Please verify and update the agent ID in `source/conf.py`."
    )
    sys.exit(1)

conf = CONF_PATH.read_text()
updated, n = re.subn(
    r"^(ai_agent_id\s*=\s*)(['\"]).*?\2",
    lambda m: f"{m.group(1)}{m.group(2)}{new_id}{m.group(2)}",
    conf,
    count=1,
    flags=re.MULTILINE,
)
if n != 1:
    print("❌ Could not find `ai_agent_id` in `source/conf.py` to update.")
    sys.exit(1)

CONF_PATH.write_text(updated)
print(f"🔁 Updated `ai_agent_id` in `source/conf.py`: {AGENT_ID} -> {new_id}")
