from pymongo import MongoClient, ASCENDING, DESCENDING
import settings
import logging
import time
logging.basicConfig(filename="log",level=logging.DEBUG)
logger = logging.getLogger( __name__ )
DB_LIKES_COUNT = "doc.likes.summary.total_count"
DB_SHARES_COUNT = "doc.shares.count"
DB_COMMENTS_COUNT = "doc.comments.summary.total_count"
DB_POST_TIME = "post_time"
DB_LAST_UPDATED = 'last_updated'
DB_NO_SHARE = {"doc.shares.count" : { '$exists': False }}
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
    def order(self, order_by):
        key = ['time', 'likes', 'comments', 'shares']


    def filter(self, d):
        # query:
        #     until_datetime: 2015/07/14
        #     since_datetime: 2015/07/07
        #     comments: 0
        #     shares: 0
        #     likes: 0
        #     order: time/likes/comments/shares
        #     total: 10
        t = time.time()
        q = {}
        if self.table:
            logger.debug("Start Querying")
            q = self.table.find(
                {"$and":[
                    {DB_LIKES_COUNT: {"$gte": d['likes']}},
                    {DB_COMMENTS_COUNT: {"$gte": d['comments']}},
                    {DB_SHARES_COUNT: {"$gte": d['shares']}}
                ]}
            )
            q.sort(DB_LIKES_COUNT,DESCENDING)
            q.limit(d['total'])
            logger.debug("Querying Time: %ss"\
            % (time.time()-t))
            return q
        else:
            logger.debug("Querying Without a Table")
            return None
def test():
    mongodb = MongoDB()
    mongodb.connect_db("fb_rawdata")
    mongodb.connect_table("posts")
    d = {}
    d['comments'] = 10
    d['shares'] = 10
    d['likes'] = 10
    d['total'] = 10
    tmp = mongodb.filter(f)
    for t in tmp:
        print(t)
# test()
