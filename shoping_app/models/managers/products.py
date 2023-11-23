from core.database import conn

db = conn['Products']


class ProductsManager():
    async def get_product_data(self):

        products_data = []
        products = db.find()

        for product in products:
            product.pop('_id')
            products_data.append(product)

        return products_data
    
    async def find_product(self, name: str):

        return db.find_one({"name": name})
    
    async def add_product(self, product: dict):

        db.insert_one(product)
