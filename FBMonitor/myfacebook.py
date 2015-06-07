import requests
import json

ID = '386669421527240'
SECRET = '11bd86cd92861bdf6ae2fd633dc38b7b'
TOKEN_URL = "https://graph.facebook.com/oauth/access_token?client_id=" + ID + "&client_secret=" + SECRET + "&grant_type=client_credentials"
BASE_URL = "https://graph.facebook.com/"

class Facebook:
    def __init__(self):
        self.token = requests.get(TOKEN_URL).text

    def get_feed(self, page_id, limit=250):
        return requests.get(BASE_URL + str(page_id) + "/posts?limit=+" + str(limit) + "+&" + self.token).text

    def get_feed_id(self, feed):
        j = json.loads(feed)
        feed_li = []
        for _feed in j['data']:
            feed_li.append(_feed['id'].split('_'))
        return feed_li

def test():
    f = Facebook()
    l = f.get_feed_id(f.get_feed(557872311000387, 5))
    print(l)

