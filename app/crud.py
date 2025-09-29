from sqlalchemy.orm import Session
from .models import Clip

def get_clips(db: Session):
    return db.query(Clip).all()

def get_clip(db: Session, clip_id: int):
    return db.query(Clip).filter(Clip.id == clip_id).first()

def increment_play_count(db: Session, clip_id: int):
    clip = db.query(Clip).filter(Clip.id == clip_id).first()
    if clip:
        clip.play_count += 1
        db.commit()
        db.refresh(clip)
    return clip
