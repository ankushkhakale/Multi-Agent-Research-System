import streamlit as st
import time
from agents.topic_suggester import TopicSuggesterAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

# Page Config
st.set_page_config(page_title="Multi-Agent Research System", page_icon="🎓", layout="wide")

# Title and Description
st.title("🎓 Multi-Agent Research System")
st.markdown("""
This system uses a team of AI agents to help you research and write IEEE standard papers.
1.  **Topic Suggester**: Suggests high-potential topics.
2.  **Researcher**: Conducts deep research.
3.  **Writer**: Drafts the paper.
4.  **Reviewer**: Reviews and critiques the draft.
""")

# Sidebar for Configuration
st.sidebar.header("Configuration")
api_key_status = "✅ Configured" # Assumes .env is set, or we could check os.getenv
st.sidebar.text(f"API Key Status: {api_key_status}")

# Initialize Agents (Cached to avoid re-initializing on every rerun)
@st.cache_resource
def load_agents():
    return {
        "suggester": TopicSuggesterAgent(),
        "researcher": ResearcherAgent(),
        "writer": WriterAgent(),
        "reviewer": ReviewerAgent()
    }

agents = load_agents()

# Main Workflow
st.header("Step 1: Choose a Topic")
area_of_interest = st.text_input("Enter your general area of interest (e.g., AI in Healthcare, Renewable Energy):")

if "suggested_topics" not in st.session_state:
    st.session_state.suggested_topics = ""

if st.button("Suggest Topics") and area_of_interest:
    with st.spinner("Topic Suggester is thinking..."):
        st.session_state.suggested_topics = agents["suggester"].suggest_topics(area_of_interest)

if st.session_state.suggested_topics:
    st.subheader("Suggested Topics")
    st.markdown(st.session_state.suggested_topics)

st.header("Step 2: Research & Write")
selected_topic = st.text_input("Enter the specific topic you want to research (copy from above or type your own):")

if st.button("Start Research & Writing") and selected_topic:
    # Research Phase
    st.subheader("🔍 Phase 1: Researching")
    with st.spinner(f"Researcher is gathering material on '{selected_topic}'..."):
        research_material = agents["researcher"].conduct_research(selected_topic)
        st.success("Research Complete!")
        with st.expander("View Research Notes"):
            st.markdown(research_material)

    # Writing Phase
    st.subheader("✍️ Phase 2: Writing Draft")
    with st.spinner("Writer is drafting the paper..."):
        paper_draft = agents["writer"].write_paper(selected_topic, research_material)
        st.success("Draft Created!")
        st.markdown("### Draft Paper")
        st.markdown(paper_draft)
        
        # Download Button for Draft
        st.download_button(
            label="Download Draft (Markdown)",
            data=paper_draft,
            file_name=f"{selected_topic.replace(' ', '_')}_draft.md",
            mime="text/markdown"
        )

    # Review Phase
    st.subheader("🧐 Phase 3: Peer Review")
    with st.spinner("Reviewer is critiquing the draft..."):
        review_feedback = agents["reviewer"].review_paper(paper_draft)
        st.success("Review Complete!")
        st.info("### Review Feedback")
        st.markdown(review_feedback)

        # Download Button for Review
        st.download_button(
            label="Download Review (Text)",
            data=review_feedback,
            file_name=f"{selected_topic.replace(' ', '_')}_review.txt",
            mime="text/plain"
        )
