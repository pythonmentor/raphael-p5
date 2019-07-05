import requests
from pprint import pprint


class ProductDownloader:

    def __init__(self):

        self._url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        self._params = {
            "tagtype_0": "categories" ,
            "tag_contains_0": "contains" ,
            "tag_0": "",
            
            "page_size": 100,
            "action": "process" ,
            "json": 1 ,
        }

    def collect(self, cat, size):
        self._params["tag_0"] = cat
        self._params["page_size"] = size
        
        response = requests.get(self._url, params=self._params)

        data = response.json()

        return data["products"]


class ProductCleaner:

    def __init__(self, products):
        
        self.products = products
        self.keys_to_keep = ["id", "product_name",  "generic_name_fr", "nutrition_grade_fr", "categories", "stores"]
        self.products_cleaned = []

    
    def clean_product(self, products):
        ''' delete_incomplete_product + delete_useless_keys '''
        
        for product in products:
            
            if set(self.keys_to_keep) <= set(product):
                if all([value for key, value in product.items() if key in self.keys_to_keep]):
                    self.products_cleaned.append(
                        {"barcode": product["id"],
                        "name": product["product_name"],
                        "description": product["generic_name_fr"],
                        "nutriscore": product["nutrition_grade_fr"],
                        "categories": product["categories"],
                        "stores": product["stores"]}
                        )
                
            

    '''def del_useless_keys(self, products_int):  # methode facultative 
        for product in products_int:
        
            product_elague = {k:v for (k,v) in product.items() if k in self.keys_to_keep} #  a chaque produit nvo dict 
            self.products_cleané.append(product_elague) # a chaque nouveau dict on append la liste des products cleané et donc elagué des k:v inutiles'''

            

"""def main():

    downloader = ProductDownloader()
    products = downloader.collect("soda", 100)

    cleaner = ProductCleaner(products)
    
    cleaner.clean_product(products)
   
    #pprint(cleaner.products_cleaned) # Test"""


if __name__ == '__main__':
    main()