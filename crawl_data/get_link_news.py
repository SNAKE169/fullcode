import requests
from bs4 import BeautifulSoup
import re
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
import uuid
import re
import codecs
import random
import datetime
from dateutil import parser
import time


pre_link = "https://www.vietnamplus.vn/"


def leng_category(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    tags = soup.findAll("div", {"class": "clearfix"})
    t = soup.findAll("span", {"id": "mainContent_ContentList1_pager"})
    return int(t[0].select('a')[-1].text)

with open('D:\Document\Python\crawl_data\\url.txt','r') as f:
    contents = f.readlines()
    for url_0 in contents:
        # print(url.strip())
        url_0 = url_0.strip()
        # url_0 = "https://www.vietnamplus.vn/doisong/lamdep.vnp"
        # print(url)
        max_leng = leng_category(url_0)
        for leng in range(1, max_leng+1):
            url = url_0[:len(url_0)-4] + f"/trang{leng}" + ".vnp"
            print(url)
            # print(url_0[:len(url)-4] + f"/trang{i}" + ".vnp")
            link_selected = set()
            result = requests.get(url)
            soup = BeautifulSoup(result.text, 'html.parser')
            tags = soup.findAll("div", {"class": "clearfix"})
            for tag in tags:
                for i in tag.select('a'):
                    link = i.get('href')
                    a = re.findall(r"[\d]+.vnp", link)
                    if(len(a) > 0):
                        link_selected.add(link)
            with open('D:\Document\Python\crawl_data\\link_news2.txt','a+', encoding='utf-8') as fi:
                for i  in link_selected:
                    fi.seek(0)
                    fi.write(pre_link + i)
                    fi.write('\n')

        # # print(link_selected)