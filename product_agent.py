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

    
    def save_product(self, product):

        self.db.query("""
            INSERT INTO Product(barcode, name, description, nutriscore, stores) 
            VALUES(:barcode, :name, :description, :nutriscore, :stores)
            ON DUPLICATE KEY UPDATE barcode=barcode, name=VALUES(name);
        """, barcode=product['barcode'], name=product['name'], description=product['description'],
            nutriscore=product['nutriscore'], stores=product['stores'])

    
    def get_prod_id(self, product):    
        
        rows = self.db.query("""
            SELECT barcode FROM Product
            WHERE name = :name
        """, name=product['name'])

        return rows
        
        
    def create_product_cat_table(self):

        self.db.query("""
        CREATE TABLE IF NOT EXISTS Product_Cat(
            product_id BIGINT UNSIGNED,
            cat_id SMALLINT UNSIGNED,
            PRIMARY KEY (product_id, cat_id),
            CONSTRAINT fk_id_product
                FOREIGN KEY(product_id)
                REFERENCES Product(barcode),
            CONSTRAINT fk_id_cat
                FOREIGN KEY (cat_id)
                REFERENCES Category(cat_id)
        )
        ENGINE = InnoDB
        """)

    
    def add_asso(self, product_id, cat_id):

        self.db.query("""
            INSERT IGNORE INTO Product_Cat(product_id, cat_id)
            VALUES(:product_id, :cat_id)
        """, product_id=product_id, cat_id=cat_id)

    
    def create_product_store_table(self):

        self.db.query("""
        CREATE TABLE IF NOT EXISTS Product_Store(
            product_id BIGINT UNSIGNED,
            store_id SMALLINT UNSIGNED,
            PRIMARY KEY (product_id, store_id),
            CONSTRAINT fk_id_product_store
                FOREIGN KEY(product_id)
                REFERENCES Product(barcode),
            CONSTRAINT fk_id_store
                FOREIGN KEY (store_id)
                REFERENCES Store(_id)
        )
        ENGINE = InnoDB
        """)
    
    
    def get_unhealthy_products(self):

        self.db.query("""
            SELECT * FROM Product
            WHERE nutriscore in ('d';'e');
        """)


