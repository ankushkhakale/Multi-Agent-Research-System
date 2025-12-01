import google.generativeai as genai
from config import MODEL_NAME, GENERATION_CONFIG

class BaseAgent:
    def __init__(self, role: str, goal: str):
        self.role = role
        self.goal = goal
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG,
            system_instruction=f"You are a {self.role}. Your goal is: {self.goal}."
        )

    def generate_response(self, prompt: str) -> str:
        """Generates a response from the agent based on the prompt."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {e}"
