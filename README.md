# 🎓 Multi-Agent Research System

A powerful AI-driven system designed to assist researchers in generating IEEE-standard research papers. This project leverages a team of specialized AI agents to handle different stages of the research process, from topic suggestion to drafting and peer review.

## 🚀 Features

The system employs a multi-agent architecture to simulate a real-world research workflow:

1.  **Topic Suggester Agent**: Suggests high-potential, practical research topics based on your area of interest. Focuses on topics with high impact and manageable innovation risk.
2.  **Researcher Agent**: Conducts deep research on the selected topic, gathering relevant information, methodologies, and context.
3.  **Writer Agent**: Synthesizes the research material into a structured IEEE-standard paper draft.
4.  **Reviewer Agent**: Acts as a peer reviewer, providing critical feedback and suggestions to improve the draft.

## 🛠️ Technology Stack

-   **Python**: Core programming language.
-   **Streamlit**: For the interactive web interface.
-   **Google Generative AI (Gemini)**: Powering the intelligence of the agents.
-   **python-dotenv**: For environment variable management.

## 📋 Prerequisites

-   Python 3.8 or higher
-   A Google Cloud API Key with access to Gemini models.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Multi-Agent-Research-System
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    -   Create a `.env` file in the root directory.
    -   Add your Google API key:
        ```env
        GOOGLE_API_KEY=your_google_api_key_here
        ```

## 🖥️ Usage

You can run the system in two modes: **Web Interface** (recommended) or **Command Line Interface (CLI)**.

### Option 1: Web Interface (Streamlit)

This provides a user-friendly interface to interact with the agents.

```bash
streamlit run app.py
```

1.  Open the URL provided in the terminal (usually `http://localhost:8501`).
2.  **Step 1**: Enter your area of interest and click "Suggest Topics".
3.  **Step 2**: Copy a topic or enter your own, then click "Start Research & Writing".
4.  The system will display progress as each agent completes its task.
5.  Download the generated **Draft Paper** and **Review Feedback**.

### Option 2: Command Line Interface (CLI)

Run the script directly in your terminal for a text-based experience.

```bash
python main.py
```

Follow the on-screen prompts to enter your area of interest and select a topic. The output files (`_draft.md` and `_review.txt`) will be saved in the current directory.

## 📂 Project Structure

```
Multi-Agent-Research-System/
├── agents/                 # Agent implementations
│   ├── base_agent.py       # Base class for agents
│   ├── researcher.py       # Researcher agent logic
│   ├── reviewer.py         # Reviewer agent logic
│   ├── topic_suggester.py  # Topic suggester logic
│   └── writer.py           # Writer agent logic
├── app.py                  # Streamlit web application
├── main.py                 # CLI entry point
├── config.py               # Configuration and API setup
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 📄 License

[MIT License](LICENSE)
