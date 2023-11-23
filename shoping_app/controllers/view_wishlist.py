from fastapi import APIRouter, Header, Request
from shoping_app.models.wishlist import Wishlist

router = APIRouter()


@router.get("", status_code=200)
async def view_wishlist(request: Request, auth_token: str = Header(alias="authorization")):

    user_data = request.user_data
    user_id = user_data.pop('_id')

    products_in_wishlist = await Wishlist.Model.objects.products_in_wishlist(user_id)
    
    return {
        "products": products_in_wishlist
    }
