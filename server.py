import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from openai import OpenAI

app = FastAPI(title="FluentKey AI prototype")
app.mount("/static", StaticFiles(directory="."), name="static")

class RewriteRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    style: str = "Natural"
    task: str = "rewrite"

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/api/rewrite")
def rewrite(req: RewriteRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="Set OPENAI_API_KEY on the server.")
    client = OpenAI(api_key=api_key)
    instructions = (
        "You are FluentKey AI, a kind English coach. Improve the user's text according "
        "to the requested task and style. Preserve meaning. Never invent facts. "
        "For explain, give a short, simple explanation and a corrected version. "
        "For translate, translate Malayalam to natural English. "
        "For reply, suggest one appropriate reply. Keep output concise. "
        "Do not add quotation marks unless needed."
    )
    prompt = f"Task: {req.task}\\nStyle: {req.style}\\nUser text:\\n{req.text}"
    try:
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
            instructions=instructions,
            input=prompt,
        )
        return {"result": response.output_text, "explanation": ""}
    except Exception as exc:
        raise HTTPException(status_code=502, detail="AI request failed. Check server configuration.") from exc
