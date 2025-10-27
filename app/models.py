from pydantic import BaseModel
from typing import List

class Quote(BaseModel):
    quote: str
    author: str
    tags: List[str]
