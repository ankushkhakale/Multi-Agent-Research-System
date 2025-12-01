import unittest
from agents.topic_suggester import TopicSuggesterAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

class TestAgents(unittest.TestCase):
    def test_topic_suggester(self):
        agent = TopicSuggesterAgent()
        response = agent.suggest_topics("Machine Learning")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertNotIn("Error generating response", response, "API Error: " + response)
        print("Topic Suggester Test Passed")

    def test_researcher(self):
        agent = ResearcherAgent()
        response = agent.conduct_research("Test Topic")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertNotIn("Error generating response", response, "API Error: " + response)
        print("Researcher Test Passed")

    def test_writer(self):
        agent = WriterAgent()
        response = agent.write_paper("Test Topic", "Test Research Material")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertNotIn("Error generating response", response, "API Error: " + response)
        print("Writer Test Passed")

    def test_reviewer(self):
        agent = ReviewerAgent()
        response = agent.review_paper("Test Paper Content")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertNotIn("Error generating response", response, "API Error: " + response)
        print("Reviewer Test Passed")

if __name__ == '__main__':
    unittest.main()
