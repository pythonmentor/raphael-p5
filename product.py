import apidownloader

class Product:

    def __init__(self, product):
        
        self.id = product["id"]
        self.product_name = product["product_name"]
        self.generic_name_fr = product["generic_name_fr"]
        self.nutrition_grade_fr = product["nutrition_grade_fr"]
        self.categories = product["categories"]
        self.stores = product["stores"]

