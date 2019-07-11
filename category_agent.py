import records

class CategoryAgent:

    def __init__(self, products_cleaned):

        self.products_cleaned = products_cleaned
        self.db = records.Database()

    
    def create_category_table(self):

        self.db.query("""
            CREATE TABLE IF NOT EXISTS Category(
            cat_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            cat_name VARCHAR(150) NOT NULL UNIQUE,
            PRIMARY KEY (cat_id)  
        )
        ENGINE = InnoDB
        """)

    
    def save_category(self, product, category):

        self.db.query("""
            INSERT INTO Category(cat_id, cat_name)
            VALUES(NULL, :cat_name)
            ON DUPLICATE KEY UPDATE cat_id=cat_id, cat_name=VALUES(cat_name);
        """, cat_name=category.strip(" "))           # A VOIR SI LE STRIP EST NECESSAIRE

    
    def get_cat_id(self, product, category):    
        
        rows = self.db.query("""
            SELECT cat_id FROM Category
            WHERE cat_name = :cat_name
        """, cat_name=category)          #product['categories'])#.split(","))

        return rows
        
        
            

            
            