import requests


class HeFeng():
    def __init__(self):
        self.url = "https://cdn.heweather.com/china-city-list.txt"
        self.encoding='utf8'
        self.pre_request="https://free-api.heweather.net/s6/weather/now?location="
        self.sub_request="&key=7ea4f7699fb14696a3dbe35d691fa928"

    def today_weather(self,city_code):
        dict=self.get_weather(city_code)
        print(dict["HeWeather6"][0]['now'])

    def get_weather(self,city_code):
        #url="https://free-api.heweather.net/s6/weather/now?location="+city_code+"&key=7ea4f7699fb14696a3dbe35d691fa928"
        url=self.pre_request+city_code+self.sub_request
        info=requests.get(url)
        info.encoding=self.encoding
        return info.json()
        #print(info.text)
    def get_city_code(self):
        cities = self.get_citys()
        for each in cities:
            yield each[2:13]

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding = self.encoding
        cities = html.text.split('\n')
        return cities[6:]


if __name__ == '__main__':
    hefeng = HeFeng()
    codes = hefeng.get_city_code()
    for i in range(10):
      #dict=hefeng.get_weather(codes.__next__())
      #print(dict["HeWeather6"][0]['now']['wind_dir'])
      hefeng.today_weather(codes.__next__())
