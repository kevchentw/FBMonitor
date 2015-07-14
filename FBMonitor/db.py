from pymongo import MongoClient, ASCENDING, DESCENDING
import FBMonitor.settings as settings
import logging
import time
import datetime
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
        key = {
            'time':DB_POST_TIME,
            'likes':DB_LIKES_COUNT,
            'comments':DB_COMMENTS_COUNT,
            'shares':DB_SHARES_COUNT
        }
        if order_by in key:
            return key[order_by]
        else:
            logger.debug("Illigal Order Key")
            return None

    def convert_date(self, start, end):
        _start = start.split("/")
        _end = end.split("/")
        start = datetime.datetime(int(_start[0]), int(_start[1]), int(_start[2]), 0, 0, 0, 0)
        end = datetime.datetime(int(_end[0]), int(_end[1]), int(_end[2]), 23, 59, 59, 0)
        return start, end

    def filter(self, d):
        t = time.time()
        q = {}
        since, until = self.convert_date(d['since_datetime'],d['until_datetime'])
        if self.table:
            logger.debug("Start Querying")
            if not d['shares']:
                q = self.table.find(
                    {"$and":[
                        DB_NO_SHARE,
                        {DB_POST_TIME: {'$gte': since, '$lte': until}},
                        {DB_LIKES_COUNT: {"$gte": int(d['likes'])}},
                        {DB_COMMENTS_COUNT: {"$gte": int(d['comments'])}},
                    ]}
                )
            else:
                q = self.table.find(
                    {"$and":[
                        {DB_LIKES_COUNT: {"$gte": int(d['likes'])}},
                        {DB_POST_TIME: {'$gte': since, '$lte': until}},
                        {DB_COMMENTS_COUNT: {"$gte": int(d['comments'])}},
                        {DB_SHARES_COUNT: {"$gte": int(d['shares'])}}
                    ]}
                )
            q.sort(self.order(d['order']),DESCENDING)
            q.limit(int(d['total']))
            logger.debug("Querying Time: %ss"\
            % (time.time()-t))
            return q
        else:
            logger.debug("Querying Without a Table")
            return None

    def filter_id(self,d):
        _posts = self.filter(d)
        logger.debug(d)
        posts = []
        counter = 0
        for p in _posts:
            counter += 1
            posts.append(p['_id'].split("_"))
        logger.debug("Items: %d" % (counter))
        return posts

def test():
    mongodb = MongoDB()
    mongodb.connect_db("fb_rawdata")
    mongodb.connect_table("posts")
    d = {}
    d['comments'] = 10
    d['shares'] = 10
    d['likes'] = 10
    d['total'] = 10
    d['order'] = 'likes'
    d['since_datetime'] = '2015/07/1'
    d['until_datetime'] = '2015/07/15'
    tmp = mongodb.filter_id(d)
    print(tmp)
# test()

def get_fb_data(d):
    mongodb = MongoDB()
    mongodb.connect_db("fb_rawdata")
    mongodb.connect_table("posts")
    return mongodb.filter_id(d)
