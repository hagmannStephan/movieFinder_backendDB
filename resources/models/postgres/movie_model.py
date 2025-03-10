from ...services.postgresql_service import Base
from sqlalchemy import (
    Column, Integer, String
)

class Movie(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True, index=True)
    original_title = Column(String(100), nullable=True)
    cover_image_src = Column(String(100), nullable=True)