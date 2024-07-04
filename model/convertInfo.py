from pydantic import BaseModel


class ConversionRequest(BaseModel):
    value: str
    from_type: str
    to_type: str