from fastapi import APIRouter, Header, Request
from shoping_app.models.add_to_cart import AddToCart

router = APIRouter()


@router.get("", status_code=200)
async def checkout(request: Request, auth_token: str = Header(alias="authorization")):

    user_data = request.user_data
    user_id = user_data.pop('_id')

    checkout_products = await AddToCart.Model.objects.products_in_cart(user_id)

    total_amount = 0

    for product in range(len(checkout_products)):
        total_amount_of_product = checkout_products[product]['price'] * checkout_products[product]['quantity']
        checkout_products[product]['amount'] = total_amount_of_product
        total_amount += total_amount_of_product
    
    return {
        "products": checkout_products,
        "total_amount": total_amount
    }
