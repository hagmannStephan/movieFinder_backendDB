from ...services.postgresql_service import Base
from sqlalchemy import (
    Column, Integer, String
)

class Movies(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True, index=True)
    original_title = Column(String(100), nullable=True)