from fastapi import APIRouter, Header, Request
from shoping_app.models.order import Orders
from shoping_app.models.add_to_cart import AddToCart
from bson import ObjectId

router = APIRouter()


@router.get("", status_code=200)
async def place_order(request: Request, auth_token: str = Header(alias="authorization")):

    user_data = request.user_data
    user_id = user_data.pop('_id')

    checkout_products = await AddToCart.Model.objects.products_in_cart(user_id)

    total_amount = 0

    for product in range(len(checkout_products)):
        total_amount_of_product = checkout_products[product]['price'] * checkout_products[product]['quantity']
        checkout_products[product]['amount'] = total_amount_of_product
        total_amount += total_amount_of_product

    await Orders.Model.objects.add_order(checkout_products, total_amount, user_id)

    await AddToCart.Model.objects.remove_products_from_cart(user_id)
    
    return {
        "message": "Your order has been placed"
    }
