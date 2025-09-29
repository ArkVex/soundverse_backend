from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Clip(Base):
    __tablename__ = "clips"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    genre = Column(String(50), nullable=False)
    duration = Column(String(10), nullable=False)
    audio_url = Column(Text, nullable=False)
    play_count = Column(Integer, default=0)
