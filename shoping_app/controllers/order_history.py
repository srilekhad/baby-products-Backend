from fastapi import APIRouter, Header, Request
from shoping_app.models.order import Orders

router = APIRouter()


@router.get("", status_code=200)
async def order_history(request: Request, auth_token: str = Header(alias="authorization")):

    user_data = request.user_data
    user_id = user_data.pop('_id')

    order_history = await Orders.Model.objects.get_order_history(user_id)
    
    return {
        "order_history": order_history
    }
