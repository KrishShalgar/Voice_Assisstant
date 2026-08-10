import os

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Read secrets/config from environment only
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
MUSIC_FILE_PATH = os.getenv("MUSIC_FILE_PATH")  # optional fallback for play music

def require_api_key():
    if not OPENWEATHER_API_KEY:
        raise RuntimeError(
            "OPENWEATHER_API_KEY not set. Set it in your environment (see README)."
        )
