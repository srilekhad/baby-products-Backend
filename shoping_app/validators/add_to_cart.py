from pydantic import BaseModel


class AddToCartRequestFormat(BaseModel):
    name: str
