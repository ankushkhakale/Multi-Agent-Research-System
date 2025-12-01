from .base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Academic Paper Writer",
            goal="Write a research paper in IEEE standard format based on provided research notes."
        )

    def write_paper(self, topic: str, research_material: str) -> str:
        prompt = f"""
        Write a full research paper on the topic: '{topic}'.
        Use the following research material:
        {research_material}

        The output MUST be in IEEE standard format structure (Abstract, Introduction, Related Work, Methodology, Results, Conclusion, References).
        You can use Markdown or LaTeX structure.
        Ensure the tone is formal and academic.
        """
        return self.generate_response(prompt)
