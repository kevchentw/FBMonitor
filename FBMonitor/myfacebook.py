import requests
import json
import time
import dateutil.parser
from FBData.models import FBData
ID = '386669421527240'
SECRET = '11bd86cd92861bdf6ae2fd633dc38b7b'
TOKEN_URL = "https://graph.facebook.com/oauth/access_token?client_id=" + ID + "&client_secret=" + SECRET + "&grant_type=client_credentials"
BASE_URL = "https://graph.facebook.com/"
SUMMARY_URL = "/posts?limit=5&fields=object_id,likes.summary(true),comments.summary(true),shares"
PAGE = ['209251989898',
        '296303767271',
        '411046232253913',
        '319186521484350',
        '598315443627319',
        '362216238522',
        '155477534498525',
        '191066727593516',
        '614665685252676',
        '518864824797451',
        '148722908483450',
        '139345196140926',
        '169299433126237',
        '167038316775699',
        '131074287040243',
        '475566682559945',
        '348527915316017',
        '129029797286279',
        '586784241439962',
        '135084993203916',
        '433317256752909',
        '416216968426055',
        '341620502649564',
        '182576165149857',
        '167116946688787',
        '237446743049832',
        '187421241309456',
        '121151784694458',
        '207857659226832',
        '247771685294517',
        '105064222931829',
        '316821618478062',
        '241947492622184',
        '142179675884434',
        '141592812610465',
        '282576301762911',
        '208898775876925',
        '222374807844875',
        '152486534850394',
        '440694596012148',
        '169748515872',
        '155010791222983',
        '114923575198147',
        '506422169398175',
        '145649977189',
        '279264471269',
        '132622800160756',
        '134469309158',
        '217633471595956']


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

    def get_summary(self, page_id):
        d = []
        print("NEW PAGE")
        meta = json.loads((requests.get(BASE_URL + str(page_id) + SUMMARY_URL + "+&" + self.token)).text)['data']
        for i in meta:
            tmp = {}
            tmp['page_id'] = i['id'].split("_")[0]
            tmp['post_id'] = i['id'].split("_")[1]
            tmp['time'] = dateutil.parser.parse(i['created_time'])
            try:
                tmp['comments'] = i['comments']['summary']['total_count']
            except:
                tmp['comments'] = 0
            try:
                tmp['likes'] = i['likes']['summary']['total_count']
            except:
                tmp['likes'] = 0
            try:
                tmp['shares'] = i['shares']['count']
            except:
                tmp['shares'] = 0
            d.append(tmp)
        return d

    def get_all_summary(self):
        d = []
        for i in PAGE:
            d += self.get_summary(i)
        FBData.objects.all().delete()
        for i in d:
            for j in i:
                data = FBData.objects.create(**i)
                print(data)
        return d

def test():
    f = Facebook()
    l = f.get_all_summary()
    print(l)


# test()
