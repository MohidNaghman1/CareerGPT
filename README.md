# 🚀 CareerGPT - Your AI-Powered Career Intelligence Platform

CareerGPT is a sophisticated, multi-agent AI assistant designed to provide comprehensive career guidance. Built with a stateful LangGraph backend and a modern Streamlit frontend, this platform helps users explore careers, create personalized learning paths, receive in-depth resume analysis, and search for real-time job openings.

---

https://github.com/MohidNaghman1/CareerGPT/issues/1#issue-3268360149


## ✨ Core Features

-   🧠 **Intelligent Agentic Workflow:** A robust "hub and spoke" design using LangGraph. A central supervisor agent intelligently routes user requests to specialized agents for different tasks.
-   🗣️ **Stateful & Context-Aware Conversations:** The application remembers context across turns, enabling advanced features like follow-up questions about an analyzed resume.
-   📚 **RAG-Powered Knowledge Base:** The `CareerAdvisor` agent uses a local FAISS vector store to provide accurate, context-aware answers to general career questions.
-   🔎 **Real-Time Job Search:** The `JobSearch` agent integrates with the Tavily Search API to find, analyze, and summarize live job postings from the internet.
-   📄 **Interactive Resume Coaching:** Upload a resume for a detailed analysis, then ask specific questions and get contextual answers from the `ResumeQAAgent`.
-   ✨ **Polished, Modern UI:** A responsive and intuitive user interface built with Streamlit and a custom, professional theme.

## 🛠️ Tech Stack

| Category      | Technology / Service                                     |
| :------------ | :------------------------------------------------------- |
| **Frontend**  | Streamlit                                                |
| **Backend**   | Python, LangChain, LangGraph                             |
| **LLMs**      | Groq (Llama 3), Google AI (Gemini for Embeddings)        |
| **Vector DB** | FAISS (Facebook AI Similarity Search)                    |
| **Tools**     | Tavily Search API                                        |

## 📂 Project Structure

```
/CareerGPT/
├── agents/
│   ├── __init__.py
│   └── chains.py             # Logic for each agent's "brain"
├── data/
│   └── career_docs/          # Source PDFs for the RAG knowledge base
├── static/
│   └── style.css             # External CSS for the UI
├── utils/
│   ├── __init__.py
│   └── file_parser.py        # PDF and DOCX parsing utility
├── .env                      # Your secret API keys (Ignored by Git)
├── .gitignore                # Specifies files/folders for Git to ignore
├── Graph_backend.py          # The core LangGraph agentic workflow
├── requirements.txt          # Project dependencies
├── setup.py                  # One-time script to build the vector store
├── streamlit_ui.py           # The main Streamlit application file
└── README.md                 # You are here!
```

---

## ⚙️ Setup and Installation

Follow these steps to get CareerGPT running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/CareerGPT.git
cd CareerGPT
```

### 2. Create and Activate a Virtual Environment
```bash
# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install all required packages using the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
You will need API keys from the following services:
-   [Groq](https://console.groq.com/keys) (for fast LLM inference)
-   [Google AI Studio](https://aistudio.google.com/app/apikey) (for text embeddings)
-   [Tavily AI](https://tavily.com/) (for the job search tool)

Create a file named `.env` in the project root. This file is included in `.gitignore` to keep your keys secure.
```env
GROQ_API_KEY="your_groq_api_key_here"
GOOGLE_API_KEY="your_google_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
```

### 5. Build the Vector Store
Before running the app, you need to build the local FAISS index from the documents in `/data/career_docs/`.
```bash
python setup.py
```
This will create a `faiss_index` folder in your project root.

### 6. Run the Application
You're all set! Launch the Streamlit app:
```bash
streamlit run streamlit_ui.py
```
Navigate to `http://localhost:8501` in your browser.

---

## 🚀 Future Enhancements

This project has a strong foundation with many possibilities for future development:

-   **Interview Coach Agent:** A new agent to conduct mock interviews and provide feedback.
-   **Persistent User Sessions:** Integrate a database (like SQLite) to save and load conversations.
-   **Advanced RAG:** Implement more sophisticated retrieval strategies like re-ranking.
-   **Long-Term Memory:** Use a vector store to give the chatbot long-term memory about the user's career goals and progress.
