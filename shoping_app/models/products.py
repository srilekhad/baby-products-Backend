from pydantic import BaseModel
from shoping_app.models.managers.products import ProductsManager


class Products(BaseModel):
    name: str
    price: float
    description: str
    image: str

    class Model:
        name = 'Products'
        objects = ProductsManager()
