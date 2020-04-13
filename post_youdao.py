import random
import time
import requests

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
        s = str(random.randint(0, 10))
        t = self.ts
        # print("random= ",s)
        # print("ts= ",t)
        # print("salt= ",t+s)
        return t + s
        # '15846844488375'

    def get_sign(self):
        e = self.content
        i = self.salt
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)
        # '51a801838d8e15397ff4f501eadf5c1b'

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_ts(self):
        ts = time.time()
        # print(ts)
        ts = str(int(round(ts * 1000)))
        # print(ts)
        # print(get_ts())
        return ts
        # '1585630699063'

    # def get_content(self):
    #    return content

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
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-637141049@10.108.160.208; OUTFOX_SEARCH_USER_ID_NCOO=840406317.6015829; JSESSIONID=aaaUFetEkXixHb9V1zYfx; ___rl__test__cookies=1586762387430',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    youdao = Youdao('黄象康')
    print(youdao.fanyi())
