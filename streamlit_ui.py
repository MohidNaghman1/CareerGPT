# streamlit_ui.py - Modern Professional Career Chatbot
import streamlit as st
import os
from langchain_core.messages import HumanMessage, AIMessage
from Graph_backend import app, AgentState
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CareerGPT - AI Career Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. MODERN PROFESSIONAL THEME ---
def load_css(file_path):
    """A helper function to load an external CSS file."""
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found at {file_path}. Please check the path.")

# --- 3. LOAD THE MODERN PROFESSIONAL THEME ---
# Provide the correct path to the CSS file inside the 'static' folder.
load_css("static/style.css")

# --- 3. BACKEND INITIALIZATION ---
@st.cache_resource
def load_backend_app():
    return app

compiled_app = load_backend_app()

# --- 4. STATE MANAGEMENT ---
def initialize_state():
    """Initialize a fresh session state."""
    st.session_state.graph_state = AgentState(
        messages=[], next="", resume_text=None
    )

if "graph_state" not in st.session_state:
    initialize_state()

# --- 5. UI COMPONENTS ---
def render_sidebar():
    """Render the modern sidebar."""
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <h2>🚀 Career Tools</h2>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📄 **Resume Analyzer**", expanded=True):
            uploaded_file = st.file_uploader(
                "Upload your resume (PDF/DOCX)", 
                type=["pdf", "docx"], 
                label_visibility="collapsed"
            )
            
            if uploaded_file:
                if st.button("🔍 Analyze Resume", type="primary", use_container_width=True):
                    with st.spinner("🧠 Processing your resume..."):
                        temp_dir = "temp_uploads"
                        os.makedirs(temp_dir, exist_ok=True)
                        file_path = os.path.abspath(os.path.join(temp_dir, uploaded_file.name))
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        st.session_state.run_prompt = f"Please analyze my resume: {file_path}"
                        st.rerun()
        
        st.markdown("---")
        
        with st.expander("⚡ **Quick Actions**", expanded=False):
            if st.button("💼 Job Market Trends", use_container_width=True):
                st.session_state.run_prompt = "What are the current job market trends in tech?"
                st.rerun()
            
            if st.button("💰 Salary Insights", use_container_width=True):
                st.session_state.run_prompt = "Give me salary insights for software engineers"
                st.rerun()
            
            if st.button("🎯 Skill Assessment", use_container_width=True):
                st.session_state.run_prompt = "Help me assess my technical skills"
                st.rerun()
        
        st.markdown("---")
        
        if st.button("🗑️ Clear Chat", type="secondary", use_container_width=True):
            initialize_state()
            st.rerun()

def display_welcome_screen():
    """Display the modern welcome interface."""
    st.markdown("""
    <div class="welcome-section">
        <h1 class="welcome-title">How Can I Accelerate Your Career?</h1>
        <p class="welcome-subtitle">Choose an area below or ask me anything about your professional journey</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Modern feature cards
    cols = st.columns(2)
    
    card_data = [
        {
            "icon": "🎯",
            "title": "Career Strategy", 
            "desc": "Get personalized career roadmaps, role comparisons, and strategic advice for your next move.",
            "prompt": "Help me create a 6-month career strategy plan",
            "key": "strategy"
        },
        {
            "icon": "🚀",
            "title": "Skill Development", 
            "desc": "Discover in-demand skills, learning paths, and certification recommendations for your field.",
            "prompt": "What skills should I learn to become a senior data scientist?",
            "key": "skills"
        },
        {
            "icon": "💼",
            "title": "Job Search", 
            "desc": "Find opportunities, optimize applications, and get insights on companies and salaries.",
            "prompt": "Find me remote software engineering jobs with high salaries",
            "key": "jobs"
        },
        {
            "icon": "🎤",
            "title": "Interview Mastery", 
            "desc": "Practice interviews, learn negotiation tactics, and get industry-specific preparation tips.",
            "prompt": "Prepare me for a technical product manager interview",
            "key": "interview"
        }
    ]
    
    for i, card in enumerate(card_data):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{card["icon"]}</div>
                <h3>{card["title"]}</h3>
                <p>{card["desc"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(card["prompt"], key=card["key"], use_container_width=True):
                st.session_state.run_prompt = card["prompt"]
                st.rerun()
    
    # Modern tip section
    st.markdown("""
    <div class="modern-tip">
        <div class="stAlert">
            <strong>💡 Pro Tip:</strong> Upload your resume using the sidebar tool for personalized career advice, 
            skill gap analysis, and tailored job recommendations based on your experience!
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_chat_history():
    """Display chat messages with modern styling."""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for message in reversed(st.session_state.graph_state['messages']):
        if isinstance(message, (HumanMessage, AIMessage)):
            with st.chat_message(message.type):
                st.markdown(message.content)
    
    st.markdown('</div>', unsafe_allow_html=True)

def handle_conversation_turn(user_prompt: str):
    """Process user input and generate AI response."""
    # Add user message
    st.session_state.graph_state['messages'].append(HumanMessage(content=user_prompt))
    
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking about your career question..."):
            response_state = compiled_app.invoke(st.session_state.graph_state)
            st.session_state.graph_state = response_state
        
        # Typing effect
        full_response = st.session_state.graph_state['messages'][-1].content
        response_placeholder = st.empty()
        buffer = ""
        
        for char in full_response:
            buffer += char
            response_placeholder.markdown(buffer + "│")
            time.sleep(0.003)
        
        response_placeholder.markdown(full_response)

def main():
    """Main application function."""
    # Modern header
    st.markdown("""
    <div class="modern-header">
        <h1>CareerGPT</h1>
        <p>Your AI-Powered Career Intelligence Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    render_sidebar()
    
    # Display appropriate screen
    if not st.session_state.graph_state['messages']:
        display_welcome_screen()
    else:
        display_chat_history()
    
    # Handle user input
    if prompt := st.chat_input("Ask me anything about your career journey..."):
        handle_conversation_turn(prompt)
    elif "run_prompt" in st.session_state and st.session_state.run_prompt:
        prompt_to_run = st.session_state.run_prompt
        st.session_state.run_prompt = None
        handle_conversation_turn(prompt_to_run)

if __name__ == "__main__":
    main()