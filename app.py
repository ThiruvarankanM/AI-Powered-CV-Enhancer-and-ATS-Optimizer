from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import tempfile
import os
from src.cv_enhancer.crew import CvEnhancer

def main():
    st.title("AI CV Enhancer")
    st.write("Upload your CV (PDF or DOCX) and get professional feedback and enhancement suggestions.")

    uploaded_file = st.file_uploader("Choose your CV file (PDF or DOCX)", type=["pdf", "docx"])
    job_description = st.text_area("Paste the job description (optional)")
    target_industry = st.text_input("Target Industry (e.g., technology, finance, healthcare)")

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            cv_path = tmp_file.name

        if st.button("Enhance My CV"):
            # Parse the CV before passing to CrewAI
            from src.cv_enhancer.tools.custom_tool import CVParseTool
            parser = CVParseTool()
            parsed_cv = parser._run(cv_path)
            inputs = {
                'cv_file': cv_path,
                'parsed_cv': parsed_cv,
                'job_description': job_description,
                'target_industry': target_industry or 'general',
                'current_year': '2025'
            }
            try:
                st.info("Processing your CV. This may take a moment...")
                result = CvEnhancer().crew().kickoff(inputs=inputs)
                st.success("CV Enhancement Complete!")
                if isinstance(result, dict) and 'Final Output' in result:
                    output = result['Final Output']
                else:
                    output = str(result)

                import re
                # Replace section headers like **References:** with bold markdown
                formatted_output = re.sub(r'\*\*([A-Za-z0-9 \-/]+):\*\*', r'**\1:**', output)
                # Optionally, add extra spacing after each section for readability
                formatted_output = re.sub(r'(\*\*[A-Za-z0-9 \-/]+:\*\*)', r'\1\n', formatted_output)
                st.markdown("### Optimized CV Output", unsafe_allow_html=True)
                st.markdown(formatted_output, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
