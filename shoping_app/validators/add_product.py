from pydantic import BaseModel


class AddProductRequestFormat(BaseModel):
    name: str
    price: float
    description: str
    image: str
