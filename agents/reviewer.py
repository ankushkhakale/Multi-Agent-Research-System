from .base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Academic Peer Reviewer",
            goal="Review research papers for IEEE standards, clarity, and technical soundness."
        )

    def review_paper(self, paper_content: str) -> str:
        prompt = f"""
        Review the following research paper draft:
        {paper_content}

        Provide a critique based on:
        1. Adherence to IEEE structure.
        2. Clarity and academic tone.
        3. Technical soundness (logic and flow).
        4. Suggestions for improvement.

        If the paper is good, explicitly state "ACCEPTED" in the summary.
        """
        return self.generate_response(prompt)
