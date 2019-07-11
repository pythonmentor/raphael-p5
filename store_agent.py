import records

class StoreAgent:

    def __init__(self, products_cleaned):

        self.products_cleaned = products_cleaned
        self.db = records.Database()

    def create_store_table(self):

        self.db.query("""
            CREATE TABLE IF NOT EXISTS Store(
            store_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(40) UNIQUE,
            PRIMARY KEY (store_id)  
        )
        ENGINE = InnoDB
        """)

    
    
    def save_store(self):
    
        self.db.query("""
            INSERT IGNORE INTO Store(store_id, name)
            VALUES(NULL, :name)
        """, name=store.strip(" "))

    
    def get_store_id(self, product, store):    
        
        rows = self.db.query("""
            SELECT store_id FROM Store
            WHERE store_name = :store_name
        """, store_name=store)
        
        for row in rows:
            store_id = row['store_id']
    