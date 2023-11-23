from pydantic import BaseModel
from shoping_app.models.managers.wishlist import WishlistManager


class Wishlist(BaseModel):
    name: str
    price: float
    description: str
    image: str

    class Model:
        name = 'Wishlist'
        objects = WishlistManager()
