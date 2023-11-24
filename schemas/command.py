import json
from typing import Optional
from pydantic import BaseModel, model_validator

class Command(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    category: str
    
    @model_validator(mode= 'before')
    @classmethod
    def model_validate_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value