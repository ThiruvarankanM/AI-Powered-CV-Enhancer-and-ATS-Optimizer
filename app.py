import streamlit as st
import tempfile
import os
import sys
sys.path.append('src')
from dotenv import load_dotenv
from cv_enhancer.crew import CvEnhancer
from cv_enhancer.tools.custom_tool import CVParseTool

load_dotenv()

st.title("🚀 AI CV Enhancer")
st.write("Upload your CV and get specific, actionable feedback based on actual content.")

uploaded_file = st.file_uploader("Choose CV file", type=["pdf", "docx"])
job_description = st.text_area("Job Description (optional)")
target_industry = st.selectbox("Target Industry", 
    ["technology", "finance", "healthcare", "marketing", "other"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        cv_path = tmp_file.name

    if st.button("Enhance CV", type="primary"):
        try:
            with st.spinner("Analyzing CV..."):
                parser = CVParseTool()
                parsed_cv = parser._run(cv_path)
                
                inputs = {
                    'cv_file': cv_path,
                    'parsed_cv': parsed_cv,
                    'job_description': job_description or 'None provided',
                    'target_industry': target_industry,
                    'current_year': '2025'
                }
                
                result = CvEnhancer().crew().kickoff(inputs=inputs)
                output = str(result)
                
                st.success("Enhancement Complete!")
                st.markdown("### Enhancement Report")
                st.markdown(output)
                
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check your .env file has OPENAI_API_KEY")
        
        finally:
            os.unlink(cv_path) if os.path.exists(cv_path) else None
