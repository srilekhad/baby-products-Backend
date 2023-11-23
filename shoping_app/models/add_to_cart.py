from pydantic import BaseModel
from shoping_app.models.managers.add_to_cart import AddToCartManager


class AddToCart(BaseModel):
    name: str
    price: float
    description: str
    image: str
    quantity: int

    class Model:
        name = 'AddToCart'
        objects = AddToCartManager()
