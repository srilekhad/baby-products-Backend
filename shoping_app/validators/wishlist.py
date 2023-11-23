from pydantic import BaseModel


class WishlistRequestFormat(BaseModel):
    name: str
