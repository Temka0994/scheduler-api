from pydantic import BaseModel, Field
from typing import Dict, Any


class NoticeSchema(BaseModel):
    body: Dict[str, Any]
    type: str
    callback: str
    status: bool = Field(default=False)
