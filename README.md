# Financial Document Analyzer - Debug Assignment

## Project Overview

This project is a **multi-agent financial document analysis system** built using **CrewAI**.  
It analyzes uploaded financial reports (PDFs) and generates structured investment insights including:

- Financial performance analysis
- Liquidity evaluation
- Risk assessment
- Investment recommendation (Buy / Hold / Sell)

The original repository contained multiple deterministic bugs and inefficient prompting issues which prevented reliable execution.  
This submission focuses on **debugging, stabilizing, and optimizing** the system while preserving the original architecture.

---

## Assignment Objectives

The challenge required fixing:

1. **Deterministic Bugs**
2. **Inefficient Prompts**

---

##  System Architecture
User Upload (FastAPI)
    ↓
PDF Processing
    ↓
CrewAI Multi-Agent Pipeline
    ↓
Structured Financial Analysis


### Agents

| Agent | Responsibility |
|------|---------------|
| Financial Analyst | Extract financial metrics & trends |
| Investment Advisor | Provide Buy/Hold/Sell recommendation |
| Risk Assessor | Identify financial & operational risks |

---

##  Bugs Found & Fixes

### 1. Tool Registration Failure
**Issue**
- Tools were passed as plain Python functions.
- CrewAI expected structured tools.

**Fix**
- Standardized tool interface.
- Implemented consistent PDF reader utility.

---

### 2. File Path Errors
**Issue**
FileNotFoundError: PDF not found


**Cause**
- Uploaded files were not handled consistently.

**Fix**
- Added dynamic file storage.
- Implemented lifecycle:


---

### 3. Circular Import Crash

**Issue**
cannot import name 'run_crew'



**Cause**
- API layer and worker logic depended on each other.

**Fix**
- Separated execution logic from API routes.

---

### 4. Agent Validation Errors

**Issue**
Input should be BaseTool


**Fix**
- Corrected CrewAI agent configuration.
- Proper tool binding implemented.


---

### 5. LLM Rate Limit Failures (Groq TPM)
**Issue**
Frequent rate limit errors due to excessive tokens.

**Root Cause**
- Large PDF context + multi-agent calls.


**Fixes**
- Limited PDF ingestion (`max_pages=3`)
- Reduced prompt verbosity
- Added execution delay
- Enforced concise outputs

Result: Stable execution.

---

### 6. Inefficient Prompt Design

**Issue**
- Excessively long responses
- Redundant reasoning
- Token waste


**Fix**
- Rewritten task prompts to enforce:
  - concise reasoning
  - document grounding
  - structured outputs

---

## Current Workflow

1. Upload financial PDF via `/analyze`
2. Extract limited document context
3. Sequential multi-agent reasoning
4. Return structured financial analysis

---

## API Usage

### Start Server

```bash
uvicorn main:app --reload

Open Swagger
http://127.0.0.1:8000/docs

```

Form Data:

file → financial PDF

query → analysis request

Example Query:

```bash
Analyze Tesla’s liquidity position and identify key financial risks.
```

```bash
{
  "status": "success",
  "analysis": "Structured financial analysis...",
  "file_processed": "TSLA-Q2-2025-Update.pdf"
}
```

## Tech Stack

FastAPI, CrewAI, Groq LLM (Llama 3.1), Python, PyPDFLoader, Pydantic

## Project Structure
```bash
project/
│
├── main.py
├── agents.py
├── task.py
├── tools.py
├── schemas.py
├── data/
└── README.md
