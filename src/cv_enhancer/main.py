#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(__file__))
from dotenv import load_dotenv
from crew import CvEnhancer
from tools.custom_tool import CVParseTool

load_dotenv()

def run():
    if len(sys.argv) < 2:
        print("Usage: python main.py <cv_file> [job_description] [industry]")
        return
    
    cv_file = sys.argv[1]
    job_desc = sys.argv[2] if len(sys.argv) > 2 else "None"
    industry = sys.argv[3] if len(sys.argv) > 3 else "technology"
    
    parser = CVParseTool()
    parsed_cv = parser._run(cv_file)
    
    inputs = {
        'parsed_cv': parsed_cv,
        'job_description': job_desc,
        'target_industry': industry
    }
    
    result = CvEnhancer().crew().kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    run()
