import records

class CategoryAgent:

    def __init__(self, products_cleaned):

        self.products_cleaned = products_cleaned
        self.db = records.Database()

    def create_category_table(self):

        self.db.query("""
            CREATE TABLE IF NOT EXISTS Category(
            _id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(150) NOT NULL UNIQUE,
            PRIMARY KEY (_id)  
        )
        ENGINE = InnoDB
        """)

    def save_category(self):

        for product in self.products_cleaned:
            for category in product["categories"].split(","):
                self.db.query("""
                    INSERT IGNORE INTO Category(_id, name)
                    VALUES(NULL, :name)
                """, name=category.strip(" "))
            