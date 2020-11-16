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
es = Elasticsearch(hosts=["https://e569e68c8281.ngrok.io"])
# def indexx(news):
#     search = es.search(index="article", body={
#         "query": {"match": {
#             "_id": news['ID']
#         }},
#         "size": 10})
#     if(len(search["hits"]["hits"]) == 0):
#         es.index(index='article', id=news['ID'], body=news)


# def beautiful_html(url):
#     tup = {}
#     tup['link'] = url
#     tup['ID'] = int(url.split("/")[-1].split('.')[0])
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, 'html.parser')
#     list_categori = []

#     if len(soup.findAll("div", {"class": "direction"})) > 0:
#         categori = soup.findAll(
#             "div", {"class": "direction"})[0].text.split("\n")

#         for i in categori:
#             if i and i != '\r':
#                 i = re.sub(r'\W+', ' ', i)
#                 list_categori.append(i)

#     if len(soup.findAll("h1", {"class": "details__headline"})) > 0:
#         details__headline = soup.findAll(
#             "h1", {"class": "details__headline"})[0].text
#         tup['title'] = details__headline
#     # print("details__headline------", details__headline)
#     if len(soup.findAll("div", {"class": "details__summary"})) > 0:
#         details__summary = soup.findAll(
#             "div", {"class": "details__summary"})[0].text
#         details__summary = re.sub(r'\W+', ' ', details__summary)
#         tup['summary'] = details__summary
#     #tup['image'] = ""
#     tup['image_title'] = ""
#     # print("details__summary-----", details__summary)
#     if(len(soup.findAll("div", {"class": "content"})) > 0):
#         content = soup.findAll("div", {"class": "content"})[0].text
#         tup['text'] = content
#     # print("content------", content)
#     list_source = []
#     if(len(soup.findAll("div", {"class": "source"})) > 0):
#         source = soup.findAll("div", {"class": "source"})[0].text.split("\n")
#         for i in source:
#             if i:
#                 list_source.append(i)
#     # print(list_source)
#         tup['author'] = list_source[0]
#     if(len(soup.findAll("div", {"class": "tags"})) > 0):
#         a = soup.findAll("div", {"class": "tags"})[0].text
#         list_x = []
#         for x in a.split("\n"):
#             if x and x != '\r':
#                 x = re.sub(r'\W+', ' ', x)
#                 list_x.append(x)
#         # print(list_x)
#         tup['tag'] = list_x
#     tup['category'] = list_categori
#     if(len(list_source) > 1):
#         date, time = list_source[1].split(" ")[:2]
#         date = date.split("/")
#         time = time + ":00"
#         date = '{}/{}/{}'.format(date[2], date[1], date[0])
#         tup['post_date'] = '{} {}'.format(date, time)

#     photos = soup.findAll("div", {"class": "article-photo"})
#     url_img = []
#     for photo in photos:
#         if(len(photo.select("img")) > 0):
#             url_img.append(photo.select("img")[0].get('src'))
#     if (len(url_img) > 0):
#         tup['image'] = url_img[0]
#     else:
#         tup['image'] = ""
#     indexx(tup)
#     print(tup['ID'])
#     return tup

# pre_link = "https://www.vietnamplus.vn/"


# def leng_category(url):
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, 'html.parser')
#     tags = soup.findAll("div", {"class": "clearfix"})
#     t = soup.findAll("span", {"id": "mainContent_ContentList1_pager"})
#     return int(t[0].select('a')[-1].text)

# with open('D:\Document\Python\crawl_data\\url.txt','r') as f:
#     contents = f.readlines()
#     for url_0 in contents:
#         # print(url.strip())
#         url_0 = url_0.strip()
#         # url_0 = "https://www.vietnamplus.vn/doisong/lamdep.vnp"
#         # print(url)
#         max_leng = leng_category(url_0)
#         for leng in range(1, max_leng+1):
#             url = url_0[:len(url_0)-4] + f"/trang{leng}" + ".vnp"
#             print(url)
#             # print(url_0[:len(url)-4] + f"/trang{i}" + ".vnp")
#             link_selected = set()
#             result = requests.get(url)
#             soup = BeautifulSoup(result.text, 'html.parser')
#             tags = soup.findAll("div", {"class": "clearfix"})
#             for tag in tags:
#                 for i in tag.select('a'):
#                     link = i.get('href')
#                     a = re.findall(r"[\d]+.vnp", link)
#                     if(len(a) > 0):
#                         link_selected.add(link)
#             for i in link_selected:
#                 beautiful_html(pre_link + i)
                    

#         # # print(link_selected)