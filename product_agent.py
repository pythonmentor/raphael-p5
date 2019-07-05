import records

class ProductAgent:

    def __init__(self, products_cleaned):

        self.products_cleaned = products_cleaned
        self.db = records.Database()

    def create_product_table(self):
        
        self.db.query("""
            CREATE TABLE IF NOT EXISTS Product(
            barcode BIGINT UNSIGNED NOT NULL,
            name VARCHAR(110) NOT NULL,
            description TEXT NOT NULL,
            nutriscore CHAR(1) NOT NULL,
            stores VARCHAR(150) NOT NULL,
            PRIMARY KEY (barcode), 
            INDEX ind_name (name),
            INDEX ind_nutri (nutriscore)
        )
        ENGINE = InnoDB
        """)

    
    def save_product(self):

        for product in self.products_cleaned:
            self.db.query("""
                INSERT INTO Product(barcode, name, description, nutriscore, stores) 
                VALUES(:barcode, :name, :description, :nutriscore, :stores)
            """, barcode=product['barcode'], name=product['name'], description=product['description'],
                nutriscore=product['nutriscore'], stores=product['stores'])


    def get_unhealthy_products(self):

        self.db.query("""
            SELECT * FROM Product
            WHERE nutriscore in ('d';'e');
        """)


