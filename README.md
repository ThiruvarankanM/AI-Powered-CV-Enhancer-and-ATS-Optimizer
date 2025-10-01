
# AI CV Enhancer & ATS Optimizer

Professional CV enhancement tool powered by CrewAI that delivers specific, actionable feedback based on your actual CV content.

## 🎯 Core Features
- **Content Analysis**: Identifies strengths, weaknesses, and project prioritization
- **Specific Feedback**: "This React project should be listed first" - not generic advice  
- **ATS Optimization**: Industry-specific keyword recommendations
- **Format Support**: PDF, DOCX file processing
- **Dual Interface**: Web app and command-line access

## 🚀 Quick Setup

```bash
git clone https://github.com/ThiruvarankanM/AI-Powered-CV-Enhancer-and-ATS-Optimizer.git
cd AI-Powered-CV-Enhancer-and-ATS-Optimizer
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file with your [free GROQ API key](https://console.groq.com):
```env
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=your_groq_api_key_here
CREWAI_TRACING_ENABLED=true
```

## 🔧 Usage

**Web Interface:**
```bash
streamlit run app.py
```

**Command Line:**
```bash
python src/cv_enhancer/main.py resume.pdf "job description" technology
```

**Quick Test:**
```bash
python test_cv.py
```

## 📋 Sample Output
```
ANALYSIS:
- Strengths: "React.js e-commerce project with 40% performance improvement"
- Priority Project: "E-commerce Platform should be listed first - shows full-stack skills"
- Improvements: Add metrics to "improved system efficiency"
- Missing Keywords: microservices, CI/CD, agile

ENHANCEMENTS:
- Project Reordering: [E-commerce Platform, Mobile App, API Development]
- Experience: "Led development team" → "Led team of 5 developers, reduced deployment time by 60%"
- Skills: Add Docker, Kubernetes for technology industry
```

## 📁 Architecture
```
AI-CV-Enhancer/           # 241 lines total, 9 files
├── app.py                # Streamlit web interface
├── test_cv.py            # Validation script
├── requirements.txt      # Dependencies (5 packages)
└── src/cv_enhancer/
    ├── crew.py           # 2-agent AI crew
    ├── main.py           # CLI interface
    ├── config/
    │   ├── agents.yaml   # CV Analyst & Writer agents
    │   └── tasks.yaml    # Analysis & enhancement tasks
    └── tools/
        └── custom_tool.py # PDF/DOCX parser
```

## 🤖 AI Agents
- **CV Analyst**: Identifies strengths, project priorities, improvement areas
- **CV Writer**: Transforms weak sections into quantified achievements

---
**Built by Thiruvarankan M** • Minimal code, maximum impact
