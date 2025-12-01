from .base_agent import BaseAgent

class TopicSuggesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Research Topic Suggester",
            goal="Suggest research topics that have high potential but are not yet fully explored (less innovation required, more practical application)."
        )

    def suggest_topics(self, area_of_interest: str) -> str:
        prompt = f"""
        Suggest 3 research topics in the field of '{area_of_interest}'.
        The topics should be:
        1. Practical and have high potential for impact.
        2. Not require groundbreaking, fundamental new science (incremental innovation is fine).
        3. Suitable for an IEEE standard paper.

        For each topic, provide:
        - Title
        - Brief Description
        - Why it has high potential
        - Why it is low risk/incremental
        """
        return self.generate_response(prompt)
