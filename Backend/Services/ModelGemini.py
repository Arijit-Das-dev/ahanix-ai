""" GEMINI """
from Backend.Config.settings import settings
from Backend.Core.Features.LLMservice import llm_service_provider
from google import genai
import os

class MODEL_GEMINI:

    def __init__(self):
        
        # Model Configuration
        self.Model = llm_service_provider.MODEL_GEMINI
        self.API_KEY = settings.GEMINI_API_KEY
        self.memory = []
        self.client = genai.Client(api_key=self.API_KEY)

        # Prompt
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        prompt_path = os.path.join(root_dir, "Prompt", "AnalystPrompt.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()