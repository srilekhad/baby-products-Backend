from fastapi import APIRouter
from shoping_app.models.products import Products

router = APIRouter()


@router.get("", status_code=200)
async def browsing():

    products_data = await Products.Model.objects.get_product_data()

    return {
        "products_data": products_data
    }
