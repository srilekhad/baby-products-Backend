from pydantic import BaseModel
from shoping_app.models.managers.order import OrdersManager


class Orders(BaseModel):
    order_details: dict
    # name: str
    # price: float
    # description: str
    # image: str
    # quantity: int

    class Model:
        name = 'Orders'
        objects = OrdersManager()
