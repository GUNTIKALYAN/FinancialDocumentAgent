from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    status: str
    query: str
    analysis: str
    file_processed: str
