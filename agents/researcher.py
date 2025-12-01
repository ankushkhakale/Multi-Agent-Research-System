from .base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Academic Researcher",
            goal="Conduct comprehensive research on a given topic to provide material for a paper."
        )

    def conduct_research(self, topic: str) -> str:
        prompt = f"""
        Conduct research on the topic: '{topic}'.
        Provide a detailed summary suitable for the following sections of an IEEE paper:
        1. Introduction (Background, Problem Statement)
        2. Related Work (Simulate citing key concepts/methods)
        3. Methodology (Proposed approach/solution)
        4. Expected Results (Hypothetical but realistic)

        Focus on technical details and academic tone.
        """
        return self.generate_response(prompt)
