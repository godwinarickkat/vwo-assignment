<<<<<<< HEAD
# 🩸 Blood Test Report Analyser API

This is a FastAPI-based intelligent report analyser that accepts blood test PDFs, extracts and analyzes the content using a team of virtual agents (Doctor, Verifier, Nutritionist, and Fitness Coach), and returns quirky, role-based summaries. The system is built with **CrewAI**, **LangChain**, and **OpenAI GPT-4**.

---

## 📌 Overview

- 📄 Upload blood test reports in PDF format
- 🧠 Analyse data with CrewAI agents
- 🤖 Powered by LangChain and OpenAI
- 🪄 Funny, imaginative, and medically-inspired responses
- 🧰 Extensible toolset for reading PDFs and searching
- 🧵 Built using FastAPI for quick testing and API interaction

---

## 🐞 Bugs Found & Fixes

| Issue | Resolution |
|-------|------------|
| ❌ Improper use of `tool` (singular) keyword in agent creation | ✅ Replaced with correct `tools=[...]` list syntax |
| ❌ `read_data_tool` async method was misused | ✅ Wrapped inside `@property` and returned a proper async function |
| ❌ Uploaded file was not saved correctly | ✅ Used `await file.read()` and `uuid4` to save file with unique names |
| ❌ `llm` object used before initialization | ✅ Instantiated `ChatOpenAI(...)` before passing it into agent constructors |
| ❌ Tasks not connected to corresponding agents | ✅ Properly assigned tasks to the respective agents with relevant tools |
| ❌ PDF text was unreadable | ✅ Switched to LangChain’s `PDFLoader` and processed the extracted text for clarity |

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **CrewAI**
- **LangChain**
- **OpenAI GPT-4**
- **Uvicorn** (for server)
- **LangChain PDFLoader**
- **Python `uuid`** for filename uniqueness

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/blood-test-analyser-debug.git
cd blood-test-analyser-debug
=======
