from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from schemas import AnalysisResponse
import os
import uuid
import time


from crewai import Crew, Process
from agents import (
    financial_analyst,
    investment_advisor,
    risk_assessor
)
from task import (
    financial_summary,
    investment_analysis,
    risk_assessment
)
from tools import read_pdf_text

app = FastAPI(title="Financial Document Analyzer")

# Crew Runner
def run_crew(query: str, file_path: str):

    try:
        # Limit pages → prevents TPM overflow
        document_text = read_pdf_text(file_path, max_pages=5)

    except Exception as e:
        raise Exception(f"Failed to read document: {str(e)}")

    crew = Crew(
        agents=[
            financial_analyst,
            investment_advisor,
            risk_assessor
        ],
        tasks=[
            financial_summary,
            investment_analysis,
            risk_assessment
        ],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff(
        inputs={
            "query": query,
            "document_text": document_text
        }
    )

    # Small delay → avoids TPM burst
    time.sleep(1)

    return result

# Routes
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document")
):

    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = run_crew(query=query, file_path=file_path)

        return AnalysisResponse(
            status="queued",
            query=query,
            analysis=str(result),
            file_processed=file.filename
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing error: {str(e)}"
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)