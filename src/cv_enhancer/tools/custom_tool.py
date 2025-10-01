from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import os
import pdfplumber
import docx

class CVParseToolInput(BaseModel):
    cv_file_path: str = Field(..., description="Path to the CV file")

class CVParseTool(BaseTool):
    name: str = "CV Parser"
    description: str = "Parse CV files and extract text content"
    args_schema = CVParseToolInput

    def _run(self, cv_file_path: str) -> str:
        ext = os.path.splitext(cv_file_path)[-1].lower()
        
        try:
            if ext == '.pdf':
                with pdfplumber.open(cv_file_path) as pdf:
                    return '\n'.join(page.extract_text() or '' for page in pdf.pages)
            elif ext in ['.docx', '.doc']:
                doc = docx.Document(cv_file_path)
                return '\n'.join(para.text for para in doc.paragraphs)
            elif ext == '.txt':
                with open(cv_file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                return "Unsupported file type"
                
        except Exception as e:
            return f"Error parsing file: {e}"
