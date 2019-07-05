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
        productagent.save_product()

        categoryagent = CategoryAgent(cleaner.products_cleaned)
        categoryagent.create_category_table()
        categoryagent.save_category()

        storeagent = StoreAgent(cleaner.products_cleaned)
        storeagent.create_store_table()
        storeagent.save_store()

        print("OK man")

if __name__ == "__main__":
    main()
