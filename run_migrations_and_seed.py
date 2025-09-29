from app.models import Base
from app.database import engine, SessionLocal
from app.seed_clips import seed_clips

# Create tables
Base.metadata.create_all(bind=engine)

# Seed clips
with SessionLocal() as db:
    seed_clips(db)
