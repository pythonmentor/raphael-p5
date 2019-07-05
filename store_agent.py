import records

class StoreAgent:

    def __init__(self, products_cleaned):

        self.products_cleaned = products_cleaned
        self.db = records.Database()

    def create_store_table(self):

        self.db.query("""
            CREATE TABLE IF NOT EXISTS Store(
            _id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(40) UNIQUE,
            PRIMARY KEY (_id)  
        )
        ENGINE = InnoDB
        """)

    def save_store(self):

        for product in self.products_cleaned:
            for store in product["stores"].split(","):
                self.db.query("""
                    INSERT IGNORE INTO Store(_id, name)
                    VALUES(NULL, :name)
                """, name=store.strip(" "))
            