from fastapi import APIRouter, Header, Request
from shoping_app.models.add_to_cart import AddToCart
from shoping_app.validators.add_to_cart import AddToCartRequestFormat

router = APIRouter()


@router.post("", status_code=200)
async def add_to_cart(request_body: AddToCartRequestFormat, request: Request, auth_token: str = Header(alias="authorization")):

    request_data = request_body.dict()

    user_data = request.user_data
    user_id = user_data.pop('_id')

    request_data['user_id'] = user_id

    products_in_cart = await AddToCart.Model.objects.add_product_to_cart(request_data['name'], user_id)
    
    return {
        "products": products_in_cart
    }


@router.delete("", status_code=200)
async def add_to_cart(request: Request, auth_token: str = Header(alias="authorization")):

    user_data = request.user_data
    user_id = user_data.pop('_id')

    await AddToCart.Model.objects.remove_products_from_cart(user_id)
    
    return {
        "message": "Products removed"
    }