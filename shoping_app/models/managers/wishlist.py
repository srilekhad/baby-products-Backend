from core.database import conn
from pydantic import validate_arguments
from shoping_app.models.products import Products

db = conn['Wishlist']


class WishlistManager:
    @validate_arguments
    async def add_product_to_wishlist(self, name: str, user_id):

        if not db.find_one({"name": name}):
            product = await Products.Model.objects.find_product(name)
            product['user_id'] = user_id
            db.insert_one(product)

        products = db.find({"user_id": user_id})

        products_in_cart = []
        for product in products:
            product.pop('_id')
            product.pop('user_id')
            products_in_cart.append(product)

        return products_in_cart
    
    @validate_arguments
    async def products_in_wishlist(self, user_id):
        
        products = db.find({"user_id": user_id})
        
        products_in_wishlist = []
        for product in products:
            product.pop('_id')
            product.pop('user_id')
            products_in_wishlist.append(product)

        return products_in_wishlist
