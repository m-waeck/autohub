# src/config.py
from utils.openai_api import get_response as openai_response
from utils.mistral_api import get_response as mistral_response
from utils.deepseek_api import get_response as deepseek_response

DEFAULT_AI_MODEL = 0

MODEL_CONFIG = {
    "ChatGPT": {
        "func": openai_response,
        "model": "gpt-3.5-turbo",
        "secret_section": "openai"
    },
    "Mistral": {
        "func": mistral_response,
        "model": "mistral-large-latest",
        "secret_section": "mistral"
    },
    "DeepSeek": {
        "func": deepseek_response,
        "model": "deepseek-chat",
        "secret_section": "deepseek"
    }
}

IMAGE_PATH = "images/autohalle-titelbild.png"
