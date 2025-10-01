
# AI CV Enhancer

Minimal CV enhancement tool using CrewAI that provides specific, actionable feedback based on actual CV content.

## Features
- Analyzes actual CV content (not generic advice)
- Identifies which projects should be prioritized
- Provides quantified improvements
- ATS optimization with specific keywords
- Supports PDF, DOCX files

## Quick Start

1. **Setup:**
```bash
git clone https://github.com/ThiruvarankanM/AI-Powered-CV-Enhancer-and-ATS-Optimizer.git
cd AI-Powered-CV-Enhancer-and-ATS-Optimizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Configure:**
Create `.env` file:
```
OPENAI_API_KEY=your_key_here
```

3. **Test:**
```bash
python test_cv.py
```

4. **Run:**
```bash
# Web interface
streamlit run app.py

# Command line
python src/cv_enhancer/main.py your_cv.pdf "job description" technology
```

## Expected Output
- **Strengths:** Specific achievements quoted from CV
- **Priority Project:** Which project should be listed first and why  
- **Improvements:** Original → Enhanced versions with metrics
- **Keywords:** Missing ATS terms for target industry

## Structure (9 files only!)
```
├── app.py              # Streamlit interface
├── test_cv.py          # Quick test  
├── requirements.txt    # Dependencies
└── src/cv_enhancer/
    ├── crew.py         # 2-agent crew
    ├── main.py         # CLI
    ├── config/
    │   ├── agents.yaml # Agent configs
    │   └── tasks.yaml  # Task configs
    └── tools/
        └── custom_tool.py # CV parser
```

Perfect for getting specific CV improvements like "This React project should be listed first because..."
