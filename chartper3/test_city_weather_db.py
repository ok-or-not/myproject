import unittest

from chartper3.city_weather import HeFeng
from chartper3.city_weather_db import HefengDb


class MyTestCase(unittest.TestCase):
    def test_something(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "huangxiangkang", "class": "net19049"})
        hefengDb.show_all()
        results = hefengDb.find({"name": "huangxiangkang"})
        for each in results:
            self.assertEqual("huangxiangkang", each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()
        # self.assertEqual(4,hefengDb.find_all())

    def test_save_all(self):
        hefeng = HeFeng()
        # codes=hefneg.get_citu_code()
        # for each in codes:
        #     print(next(codes))

        each = hefeng.get_weather("CN101010200")
        print(each)
        hefengDB = HefengDb()
        hefengDB.save(each)


if __name__ == '__main__':
    unittest.main()
