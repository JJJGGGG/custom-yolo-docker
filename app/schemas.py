from pydantic import BaseModel
from typing import List, Tuple, Optional

class YoloBody(BaseModel):
    image: str
