import random
import time
import json
import requests
import hashlib

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content = '我和你'


class Youdao():
    def __init__(self,content):
        self.content = content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_sign(self):
        i = self.salt
        s = "fanyideskweb" + self.content + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_md5(self, value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_ts(self):
        ts = time.time()
        ts = str(int(round(ts * 1000)))
        return ts

    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '0ed2e07b89acaa1301d499442c9fdf79',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def get_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-637141049@10.108.160.208; OUTFOX_SEARCH_USER_ID_NCOO=840406317.6015829; JSESSIONID=aaaUFetEkXixHb9V1zYfx; ___rl__test__cookies=1586762387430',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
  while(True):
    a=input("Please input what words do you want to translate ：")
    youdao = Youdao(a)
    print("fanyi result  :",youdao.fanyi())