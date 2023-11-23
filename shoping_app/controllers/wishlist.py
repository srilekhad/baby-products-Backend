from fastapi import APIRouter, Header, Request
from shoping_app.models.wishlist import Wishlist
from shoping_app.validators.wishlist import WishlistRequestFormat

router = APIRouter()


@router.post("", status_code=200)
async def add_to_wishlist(request_body: WishlistRequestFormat, request: Request, auth_token: str = Header(alias="authorization")):

    request_data = request_body.dict()

    user_data = request.user_data
    user_id = user_data.pop('_id')

    products_in_cart = await Wishlist.Model.objects.add_product_to_wishlist(request_data['name'], user_id)
    
    return {
        "products": products_in_cart
    }
