#!/usr/bin/env python3
import sys
import os
sys.path.append('src')

try:
    import streamlit, crewai, pdfplumber, docx
    from cv_enhancer.tools.custom_tool import CVParseTool
    
    # Quick test
    with open('temp.txt', 'w') as f:
        f.write("John Doe\nSoftware Engineer")
    
    parser = CVParseTool()
    result = parser._run('temp.txt')
    os.remove('temp.txt')
    
    print("✅ Ready! Run: streamlit run app.py")
    
except Exception as e:
    print(f"❌ Error: {e}")