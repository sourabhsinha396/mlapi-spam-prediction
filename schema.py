from pydantic import BaseModel, Field


class Input(BaseModel):
    input: str = Field(min_length=1)