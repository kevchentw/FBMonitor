from pymongo import MongoClient
import settings
import logging
logging.basicConfig(filename="log",level=logging.DEBUG)
logger = logging.getLogger( __name__ )

class MongoDB:
    def __init__(self):
        self.connect()
        self.db = None
        self.table = None
    def connect(self):
        url = 'mongodb://%s:%s@%s'\
        % (settings.DB_USERNAME,settings.DB_PASSWORD,settings.DB_ADDRESS)
        self.connection = MongoClient(url)
        logger.debug("Connect to MangoDB: Success!")
    def connect_db(self, db_name):
        self.db = self.connection[db_name]
        logger.debug("Connect to DB: " + db_name)
    def connect_table(self, table_name):
        if self.db:
            self.table = self.db[table_name]
            logger.debug("Connect to Table: " + table_name)
        else:
            logger.debug("Connect to Table without choosing DB")
    def filter(self):
        q = {}
        if self.table:
            q = self.table.find_one()
        return q
def test():
    mongodb = MongoDB()
    mongodb.connect_db("test_kaogaau")
    mongodb.connect_table("posts")
    tmp = mongodb.filter()
    print(tmp)
test()
