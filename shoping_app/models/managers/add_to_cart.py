from core.database import conn
from pydantic import validate_arguments
from shoping_app.models.products import Products

db = conn['AddToCart']


class AddToCartManager:
    @validate_arguments
    async def add_product_to_cart(self, name: str, user_id):

        product = await Products.Model.objects.find_product(name)
        if not db.find_one({"name": name}):
            product['user_id'] = user_id
            product['quantity'] = 1
            db.insert_one(product)
        else:
            update_query = {"$inc": {"quantity": 1}}
            db.update_one({"name": name}, update_query)

        products = db.find({"user_id": user_id})

        products_in_cart = []
        for product in products:
            product.pop('_id')
            product.pop('user_id')
            products_in_cart.append(product)

        return products_in_cart
    
    @validate_arguments
    async def products_in_cart(self, user_id):
        
        products = db.find({"user_id": user_id})
        
        products_in_cart = []
        for product in products:
            product.pop('_id')
            product.pop('user_id')
            products_in_cart.append(product)

        return products_in_cart

    async def remove_products_from_cart(self, user_id):

        filter_query = {"user_id": user_id}

        result = db.delete_many(filter_query)
