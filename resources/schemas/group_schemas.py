from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import date

class Group(BaseModel):
    group_id: int
    name: str = Field(..., max_length=25)
    password: str = Field(..., max_length=50)
    admin_id: int
    created_on: date

    show_movies: bool = True
    show_tv: bool = True
    include_adult: bool = False
    language: str = Field(default='en-US', max_length=10)
    release_date_gte: Optional[date] = Field(default='1900-01-01')
    release_date_lte: Optional[date] = Field(default='now()')
    watch_region: Optional[str] = Field(default='CH', max_length=10)
    watch_providers: Optional[List] = Field(default_factory=list)
    with_genres: Optional[List] = Field(default_factory=list)
    without_genres: Optional[List] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)