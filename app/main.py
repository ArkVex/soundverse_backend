from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import requests
import tempfile
from starlette_exporter import PrometheusMiddleware, handle_metrics

from .database import SessionLocal
from .crud import get_clips, get_clip, increment_play_count
from .schemas import ClipOut


app = FastAPI(title="Soundverse Clips Backend")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/clips", response_model=list[ClipOut])
def list_clips(db: Session = Depends(get_db)):
    clips = get_clips(db)
    return clips

from fastapi.responses import RedirectResponse

@app.get("/clips/{clip_id}/stream")
def stream_clip(clip_id: int, db: Session = Depends(get_db)):
    clip = get_clip(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    increment_play_count(db, clip_id)
    return RedirectResponse(clip.audio_url)

@app.get("/clips/{clip_id}/stats", response_model=ClipOut)
def clip_stats(clip_id: int, db: Session = Depends(get_db)):
    clip = get_clip(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    return clip
