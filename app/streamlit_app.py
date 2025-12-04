import streamlit as st
import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ResearchAssistant

st.set_page_config(page_title="Multi-Agent Research Assistant", layout="wide")

st.title("🤖 Multi-Agent Research Assistant")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Groq API Key", type="password")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
        
    st.markdown("---")
    st.markdown("### How it works")
    st.markdown("1. **Planner**: Breaks down query")
    st.markdown("2. **Search**: Scrapes web/docs")
    st.markdown("3. **Retriever**: Finds relevant info")
    st.markdown("4. **Critic**: Validates facts")
    st.markdown("5. **Writer**: Generates report")

# Main Interface
query = st.text_area("Enter your research topic:", height=100)

if st.button("Start Research"):
    if not query:
        st.warning("Please enter a query.")
    elif not os.environ.get("GROQ_API_KEY"):
        st.error("Please provide a Groq API Key.")
    else:
        with st.spinner("Researching... This may take a few minutes."):
            try:
                assistant = ResearchAssistant()
                report = assistant.run_research(query)
                
                st.success("Research Complete!")
                
                tab1, tab2 = st.tabs(["📄 Report", "💾 Download"])
                
                with tab1:
                    st.markdown(report)
                    
                with tab2:
                    st.download_button(
                        label="Download Report (Markdown)",
                        data=report,
                        file_name="research_report.md",
                        mime="text/markdown"
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")

# File Upload Section (Optional extension)
st.markdown("---")
st.header("📂 Upload Documents (Optional)")
uploaded_file = st.file_uploader("Upload a PDF for context", type=["pdf"])
if uploaded_file:
    # Logic to handle file upload and indexing would go here
    # For now, just a placeholder
    st.info("File uploaded. (Integration pending)")
