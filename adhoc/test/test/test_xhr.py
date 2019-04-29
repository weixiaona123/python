# coding:utf-8
# from bs4 import BeautifulSoup
import requests
import json
import pymongo

url = 'http://192.168.218.55:8080/adhoc_test_h5editor/a.html'


def dealData(url):
    client = pymongo.MongoClient('localhost', 27017)
    # guoke = client['guoke']
    # guokeData = guoke['guokeData']
    web_data = requests.get(url)
    print(web_data)
    datas = json.loads(web_data.text)
    print(datas)
    datas.keys()
    # for data in datas['result']:
    #     guokeData.insert_one(data)


def start():
    urls = [
        'http://192.168.218.55:8080/adhoc_test_h5editor/a.html'.format(
            str(i)) for i in range(20, 100, 20)]
    for url in urls:
        dealData(url)


start()
