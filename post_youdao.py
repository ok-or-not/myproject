import random
import time
import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
   s=str(random.randint(0,10))
   t=get_ts()
   #print("random= ",s)
   #print("ts= ",t)
   #print("salt= ",t+s)
   return t+s
      #'15846844488375'


def get_sign():
   return '51a801838d8e15397ff4f501eadf5c1b'


def get_ts():
   ts = time.time()
   #print(ts)
   ts = str(int(round(ts * 1000)))
   #print(ts)
   #print(get_ts())
   return ts
         #'1585630699063'

from_data={
   'i':'我和你',
   'from':'AUTO',
   'to':'AUTO',
   'smartresult':'dict',
   'client':'fanyideskweb',
   'salt': get_salt(),
   'sign': get_sign(),
   'ts': get_ts(),
   'bv':'0ed2e07b89acaa1301d499442c9fdf79',
   'doctype':'json',
   'version':'2.1',
   'keyfrom':'fanyi.web',
   'action':'FY_BY_REALTlME',
}
response=requests.post(url,from_data)
print(response.text)