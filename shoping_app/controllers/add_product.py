from fastapi import APIRouter
from shoping_app.models.products import Products
from shoping_app.validators.add_product import AddProductRequestFormat

router = APIRouter()


@router.post("", status_code=200)
async def add_product(request_body: AddProductRequestFormat):

    request_data = request_body.dict()

    await Products.Model.objects.add_product(request_data)
    
    return {
        "message": "Your product has been added"
    }
