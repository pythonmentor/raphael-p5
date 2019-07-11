from apidownloader import *
from product_agent import *
from category_agent import *
from store_agent import *


def main():

        downloader = ProductDownloader()

        cat = ["soda", "pizzas tartes salées et quiches", "biscuits et gâteaux", "céréales pour petit-déjeuner", "plats préparés à réchauffer au micro-ondes", "Salades composées"]
        products = [product for keyword in cat for product in downloader.collect(keyword, 100)]
        
        cleaner = ProductCleaner(products)
        cleaner.clean_product(products)


        productagent = ProductAgent(cleaner.products_cleaned)
        productagent.create_product_table()
        
        categoryagent = CategoryAgent(cleaner.products_cleaned)
        categoryagent.create_category_table()
        
        productagent.create_product_cat_table()

        #storeagent = StoreAgent(cleaner.products_cleaned)
        #storeagent.create_store_table()
        
        #productagent.create_product_store_table()


        
        for product in productagent.products_cleaned:
                productagent.save_product(product)
                rows = productagent.get_prod_id(product)
                
                for row in rows:
                        product_id = row['barcode']
                        
                
                for category in product["categories"].split(","):
                        categoryagent.save_category(product, category)
                        rows = categoryagent.get_cat_id(product, category)
                        
                        for row in rows:
                                cat_id = row['cat_id']

                if product_id and cat_id:
                        productagent.add_asso(product_id, cat_id)

                #for store in product["stores"].split(","):
                        #storeagent.save_store(product, store)

        
        

        

        #storeagent = StoreAgent(cleaner.products_cleaned)
        #storeagent.create_store_table()
        #productagent.create_product_store_table()
        #
        
        print("OK man")

if __name__ == "__main__":
    main()
