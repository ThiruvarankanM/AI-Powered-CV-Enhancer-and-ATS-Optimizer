from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

# For PDF and DOCX parsing
import pdfplumber
import docx

class CVParseToolInput(BaseModel):
    """Input schema for CVParseTool."""
    cv_file_path: str = Field(..., description="Path to the CV file (PDF or DOCX).")

class CVParseTool(BaseTool):
    name: str = "CV Parser Tool"
    description: str = (
        "Parses a CV file (PDF or DOCX) and extracts structured information such as contact details, education, experience, and skills."
    )
    args_schema: Type[BaseModel] = CVParseToolInput

    def _run(self, cv_file_path: str) -> str:
        ext = os.path.splitext(cv_file_path)[-1].lower()
        if ext == '.pdf':
            text = self._parse_pdf(cv_file_path)
        elif ext in ['.docx', '.doc']:
            text = self._parse_docx(cv_file_path)
        else:
            return "Unsupported file type. Please upload a PDF or DOCX CV."
        # Simple section extraction (can be improved)
        sections = self._extract_sections(text)
        return sections

    def _parse_pdf(self, file_path: str) -> str:
        try:
            with pdfplumber.open(file_path) as pdf:
                return '\n'.join(page.extract_text() or '' for page in pdf.pages)
        except Exception as e:
            return f"Error reading PDF: {e}"

    def _parse_docx(self, file_path: str) -> str:
        try:
            doc = docx.Document(file_path)
            return '\n'.join([para.text for para in doc.paragraphs])
        except Exception as e:
            return f"Error reading DOCX: {e}"

    def _extract_sections(self, text: str) -> str:
        # Very basic section extraction by keywords
        sections = {}
        current_section = 'Other'
        for line in text.split('\n'):
            line_strip = line.strip()
            if not line_strip:
                continue
            if any(h in line_strip.lower() for h in ['contact', 'email', 'phone']):
                current_section = 'Contact'
            elif 'education' in line_strip.lower():
                current_section = 'Education'
            elif 'experience' in line_strip.lower():
                current_section = 'Experience'
            elif 'skill' in line_strip.lower():
                current_section = 'Skills'
            elif 'summary' in line_strip.lower():
                current_section = 'Summary'
            sections.setdefault(current_section, []).append(line_strip)
        # Format output
        output = []
        for sec, lines in sections.items():
            output.append(f"## {sec}\n" + '\n'.join(lines))
        return '\n\n'.join(output)
