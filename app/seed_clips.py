from sqlalchemy.orm import Session
from .models import Clip

# Replace these URLs with actual public domain MP3 links
CLIPS = [
    {
        "title": "Ambient Sunrise",
        "description": "Gentle ambient music for a calm morning.",
        "genre": "ambient",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7e7.mp3"
    },
    {
        "title": "Pop Groove",
        "description": "Upbeat pop track for energetic vibes.",
        "genre": "pop",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7e8.mp3"
    },
    {
        "title": "Electronic Pulse",
        "description": "Driving electronic beat for focus.",
        "genre": "electronic",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7e9.mp3"
    },
    {
        "title": "Chill Vibes",
        "description": "Relaxing chillhop for study sessions.",
        "genre": "ambient",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7ea.mp3"
    },
    {
        "title": "Funky Bass",
        "description": "Funky bass groove for fun times.",
        "genre": "pop",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7eb.mp3"
    },
    {
        "title": "Epic Journey",
        "description": "Cinematic score for adventure.",
        "genre": "electronic",
        "duration": "30s",
        "audio_url": "https://cdn.pixabay.com/audio/2022/10/16/audio_12b6b1b7ec.mp3"
    }
]

def seed_clips(db: Session):
    for clip in CLIPS:
        db.add(Clip(**clip))
    db.commit()
