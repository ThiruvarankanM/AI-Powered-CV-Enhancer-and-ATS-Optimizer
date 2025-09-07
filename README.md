
# AI-Based CV Enhancer (CrewAI)

This project is a professional, multi-agent AI system for analyzing, critiquing, and optimizing real user CVs. Built on [CrewAI](https://crewai.com), it provides actionable, personalized feedback and ATS (Applicant Tracking System) optimization for job seekers.

## Features
- Upload your CV (PDF or DOCX) and receive detailed, section-by-section analysis.
- Agents provide specific feedback, quote your real CV, and suggest improvements.
- ATS optimization tips tailored to your content.
- Industry-specific advice for your target job sector.
- Token-efficient: only the most relevant CV sections are processed.
- Switch LLM providers (Groq, Gemini, OpenAI, Ollama) via `.env`.

## Project Structure

```
├── app.py                  # Streamlit web app for user interaction
├── src/
│   └── cv_enhancer/
│       ├── crew.py         # CrewAI workflow, agent/task definitions
│       ├── main.py         # CLI entry point
│       ├── config/
│       │   ├── agents.yaml # Agent roles, goals, backstories
│       │   └── tasks.yaml  # Task instructions and outputs
│       └── tools/
│           └── custom_tool.py # CV parsing tool (PDF/DOCX)
├── .env                    # LLM provider/model/API key
├── requirements.txt        # Python dependencies
```

## Installation

1. **Clone the repository**
2. **Set up a virtual environment**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```
3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```
4. **Configure `.env`**
	- Set your LLM provider, model, and API key. Example:
	  ```
	  PROVIDER=groq
	  MODEL=llama-3.3-70b-versatile
	  GROQ_API_KEY=your_groq_api_key_here
	  ```

## Usage

### Web App (Recommended)
Run the Streamlit app:
```bash
streamlit run app.py
```
Upload your CV, enter job info, and view detailed, actionable feedback.

### Command-Line Interface
Run the workflow from the terminal:
```bash
python src/cv_enhancer/main.py <cv_file_path> [job_description_path_or_text] [target_industry]
```

## How It Works

1. **CV Upload/Parsing:** Your CV is parsed (PDF/DOCX) and split into sections (Summary, Experience, Skills, etc.).
2. **Multi-Agent Analysis:**
	- Analyzer: Quotes and critiques each section, states if it's strong/weak/missing, and suggests improvements.
	- Content Writer: Rewrites only weak/missing sections, showing before/after.
	- ATS Optimizer: Gives specific, actionable tips for ATS compatibility, referencing your real content.
	- Industry Expert: Provides sector-specific advice, quoting your actual CV.
3. **Token Optimization:** Only the most relevant CV sections are sent to the LLM, reducing cost and avoiding rate limits.
4. **Provider Flexibility:** Easily switch LLMs by editing `.env`.

## Customization
- Edit `src/cv_enhancer/config/agents.yaml` to change agent roles or goals.
- Edit `src/cv_enhancer/config/tasks.yaml` to change task instructions or outputs.
- Edit `src/cv_enhancer/tools/custom_tool.py` to improve CV parsing or section extraction.
- Edit `.env` to change LLM provider/model/API key.

## Support

- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

---
This project demonstrates a professional, real-world use of CrewAI for personalized, actionable CV enhancement. Contributions and feedback are welcome!
