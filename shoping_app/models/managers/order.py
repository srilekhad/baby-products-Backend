from core.database import conn

db = conn['Orders']


class OrdersManager():
    async def get_order_history(self, user_id):

        order_history = []
        orders = db.find({'user_id': user_id})

        for order in orders:
            order.pop('_id')
            order.pop('user_id')
            order_history.append(order)

        return order_history
    
    async def add_order(self, product: list, total_cost: int, user_id):

        db.insert_one({
            "order_list": product,
            "total_cost": total_cost,
            "user_id": user_id
        })
