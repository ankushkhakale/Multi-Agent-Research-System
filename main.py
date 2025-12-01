import os
from agents.topic_suggester import TopicSuggesterAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

def main():
    print("Welcome to the Multi-Agent Research System (IEEE Standard)")
    print("---------------------------------------------------------")

    # Initialize Agents
    suggester = TopicSuggesterAgent()
    researcher = ResearcherAgent()
    writer = WriterAgent()
    reviewer = ReviewerAgent()

    # Step 1: Topic Suggestion
    area_of_interest = input("\nEnter your general area of interest (e.g., AI in Healthcare): ")
    print(f"\n[Topic Suggester] Generating topics for '{area_of_interest}'...")
    topics = suggester.suggest_topics(area_of_interest)
    print(f"\nSuggested Topics:\n{topics}")

    # Step 2: Topic Selection
    selected_topic = input("\nEnter the specific topic you want to research from the list above: ")

    # Step 3: Research
    print(f"\n[Researcher] Conducting research on '{selected_topic}'...")
    research_material = researcher.conduct_research(selected_topic)
    print("\nResearch Material Gathered.")
    # print(research_material) # Optional: Print research notes

    # Step 4: Writing
    print(f"\n[Writer] Drafting IEEE paper on '{selected_topic}'...")
    paper_draft = writer.write_paper(selected_topic, research_material)
    print("\nPaper Draft Created.")
    
    # Save Draft
    draft_filename = f"{selected_topic.replace(' ', '_')}_draft.md"
    with open(draft_filename, "w", encoding='utf-8') as f:
        f.write(paper_draft)
    print(f"Draft saved to {draft_filename}")

    # Step 5: Review
    print(f"\n[Reviewer] Reviewing the draft...")
    review_feedback = reviewer.review_paper(paper_draft)
    print(f"\nReview Feedback:\n{review_feedback}")

    # Save Review
    review_filename = f"{selected_topic.replace(' ', '_')}_review.txt"
    with open(review_filename, "w", encoding='utf-8') as f:
        f.write(review_feedback)
    print(f"Review saved to {review_filename}")

    print("\nProcess Complete!")

if __name__ == "__main__":
    main()
