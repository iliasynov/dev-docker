from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse, RedirectResponse
import os

app = FastAPI(title="Docker Cloud Backend")

# For dev: allow everything. Later you can restrict to your frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONT_URL = os.getenv("FRONT_URL", "http://localhost:8080")

@app.get("/", include_in_schema=False)
def go_to_front():
    # "Calls" / redirects to the frontend
    return RedirectResponse(url=FRONT_URL)

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"

@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "ok"
