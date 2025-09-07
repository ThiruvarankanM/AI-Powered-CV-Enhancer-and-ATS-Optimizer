from dotenv import load_dotenv
load_dotenv()
#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from cv_enhancer.crew import CvEnhancer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        CvEnhancer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def run():
    """
    Run the CV enhancement workflow.
    """
    import sys
    from src.cv_enhancer.tools.custom_tool import CVParseTool
    if len(sys.argv) < 2:
        print("Usage: python main.py <cv_file_path> [job_description_path] [target_industry]")
        sys.exit(1)
    cv_file = sys.argv[1]
    job_description = ''
    if len(sys.argv) > 2:
        job_description = open(sys.argv[2]).read() if os.path.exists(sys.argv[2]) else sys.argv[2]
    target_industry = sys.argv[3] if len(sys.argv) > 3 else 'general'
    current_year = str(datetime.now().year)
    parser = CVParseTool()
    parsed_cv = parser._run(cv_file)
    inputs = {
        'cv_file': cv_file,
        'parsed_cv': parsed_cv,
        'job_description': job_description,
        'target_industry': target_industry,
        'current_year': current_year
    }
    try:
        CvEnhancer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the CV enhancer crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CvEnhancer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def train():
    """
    Train the CV enhancer crew for a given number of iterations.
    """
    cv_file = 'path/to/cv.pdf'
    job_description = 'path/to/job_description.txt'
    target_industry = 'technology'
    current_year = str(datetime.now().year)
    inputs = {
        'cv_file': cv_file,
        'job_description': job_description,
        'target_industry': target_industry,
        'current_year': current_year
    }
    try:
        CvEnhancer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the CV enhancer crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CvEnhancer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def replay():
    """
    Replay the CV enhancement workflow from a specific task.
    """
    try:
        CvEnhancer().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the CV enhancer crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CvEnhancer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def test():
    """
    Test the CV enhancement workflow and return the results.
    """
    cv_file = 'path/to/cv.pdf'
    job_description = 'path/to/job_description.txt'
    target_industry = 'technology'
    current_year = str(datetime.now().year)
    inputs = {
        'cv_file': cv_file,
        'job_description': job_description,
        'target_industry': target_industry,
        'current_year': current_year
    }
    try:
        CvEnhancer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the CV enhancer crew: {e}")
