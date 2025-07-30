"""FastAPI entrypoint."""

from fastapi import FastAPI
from pydantic import BaseModel

from controller import run_job

app = FastAPI()


n_workers = 0


class JobRequest(BaseModel):
    prompt: str


@app.post("/run_job")
async def run_job_endpoint(req: JobRequest) -> dict:
    count = run_job(req.prompt)
    return {"count": count}
