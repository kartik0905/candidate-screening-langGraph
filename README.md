# 🧑‍💼 Candidate Screening Workflow with LangGraph

This project is an **AI-powered candidate screening system** built with [LangGraph](https://python.langchain.com/docs/langgraph/), [LangChain](https://www.langchain.com/), and OpenAI.  
It automatically evaluates job applications, categorizes candidates by **experience level**, checks for a **skill match**, and then decides whether to:  

- ✅ Shortlist for HR interview  
- 📈 Escalate to a recruiter  
- ❌ Send a rejection email  

---

## ✨ Features
- **State machine workflow** with LangGraph  
- **Experience level classification** (`Entry-level | Mid-level | Senior-level`)  
- **Skillset assessment** (`Match | No Match`)  
- **Dynamic routing** (HR → Recruiter → Rejection)  
- **Extensible design** – easily adapt prompts for other job roles  

---

## 🛠 Tech Stack
- [Python 3.10+](https://www.python.org/)  
- [LangGraph](https://python.langchain.com/docs/langgraph/)  
- [LangChain](https://www.langchain.com/)  
- [OpenAI / ChatOpenAI](https://platform.openai.com/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 📂 Folder Structure
```
.
├── main.py   # Main workflow
├── .env                     # Stores API keys (ignored in git)
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/<your-username>/candidate-screening.git
   cd candidate-screening
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add API key**  
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

Run the workflow with a sample candidate application:

```bash
python main.py
```

### Example Output
```
Categorizing the experience level of the candidate
Assessing the skillset of candidate :
Skill Match : No Match
Sending Rejection Email


Computed Results :
Application: I have 10 years of experience in software engineering with expertise in C#
Experience Level: Senior-level
Skill Match: No Match
Response: Candidate has been escalated to the recruiter.
```

---

## 🔮 Future Improvements
- ✅ Structured output parsing (guarantee clean values)  
- ✅ Configurable job roles instead of hardcoding "Python Developer"  
- ✅ Error handling & validation  
- ✅ REST API / frontend integration  

---

## 🤝 Contributing
Feel free to fork this repo and submit PRs with improvements 🚀

---

## 📜 License
MIT License © 2025 [Kartik Garg]  
