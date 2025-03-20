import os
import json
from streamlit import set_page_config


set_page_config(
    page_title="Buffalo Theater Aggregator",
    page_icon="🎭",
    layout="wide",
    menu_items={
        "Report a bug": "https://github.com/mjlabe/buffalo_theater_shows/issues",
    },
)


graph_config = {
    "llm": {
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini",
        "max_tokens": 4096
    },
    "verbose": True,
    "headless": True,
}


with open(os.environ.get("sites_path", "/src/sites.json")) as f:
    sites = json.load(f).get("sites", [])
