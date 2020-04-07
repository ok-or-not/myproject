import unittest
from unittest import mock

from post_youdao import *


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        # import time
        # ts=time.time()
        # print(ts)
        # ts=str(int(round(ts*1000)))
        # print(ts)
        # print(get_ts())
        get_ts=mock.Mock(return_value='1584684448837')
        self.assertEqual('1584684448837',get_ts())
    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15846844488375')
        self.assertEqual('15846844488375',get_salt())
    def test_get_sign(self):
        self.assertEqual('51a801838d8e15397ff4f501eadf5c1b',get_sign())



if __name__ == '__main__':
    unittest.main()
