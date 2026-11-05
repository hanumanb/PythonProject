
from fastapi import FastAPI
from pydantic import BaseModel, Field

from .analyzer import analyze_lines

app = FastAPI(title="SRE Log Analyzer", version="1.0.0")

class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=1, max_length=200_000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    incidents = analyze_lines(request.text.splitlines())
    return {"incident_count": len(incidents),
            "incidents": [incident.to_dict() for incident in incidents]}
