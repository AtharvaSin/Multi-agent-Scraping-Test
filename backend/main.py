"""FastAPI entrypoint."""

from fastapi import FastAPI, Response
from pydantic import BaseModel

from .controller import run_job
from .storage_manager import fetch_items
import csv
from io import StringIO

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


n_workers = 0


class JobRequest(BaseModel):
    prompt: str


@app.post("/run_job")
async def run_job_endpoint(req: JobRequest) -> dict:
    count, items = run_job(req.prompt)
    return {"count": count, "items": items}


@app.get("/data")
async def get_data() -> list[dict]:
    return fetch_items()


@app.get("/data_csv")
async def get_data_csv() -> Response:
    items = fetch_items()
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(items)
    csv_data = output.getvalue()
    headers = {
        "Content-Disposition": "attachment; filename=data.csv",
        "Content-Type": "text/csv",
    }
    return Response(content=csv_data, media_type="text/csv", headers=headers)
