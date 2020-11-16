from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def write_an_article(url):
    # url = "https://www.vietnamplus.vn/thu-tuong-cong-an-can-coi-danh-du-la-dieu-thieng-lieng-cao-quy-nhat/657800.vnp"
    # url = "https://www.vietnamplus.vn//le-vieng-va-mo-so-tang-nguyen-tong-bi-thu-le-kha-phieu-tai-ch-sec/657832.vnp"
    with open('D:\Document\Python\crawl_data\\tieude.txt','a+', encoding = 'utf-8') as tx:
        tx.write(url)
        tx.write('\n')
    with open('D:\Document\Python\crawl_data\\text.txt','a+', encoding = 'utf-8') as tx:
        tx.write('\n')
        tx.write(url)
        tx.write('\n\n')
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('p')
    for line in tag:
        txtt = line.get_text()
        #print(txtt)
        with open('D:\Document\Python\crawl_data\\text.txt','a+', encoding = 'utf-8') as tx:
            tx.seek(0)
            if("Ảnh" not in txtt):
                tx.write(line.get_text())
                tx.write('\n')
for i in range(1,4):
    url = "https://www.vietnamplus.vn/chinhtri/trang{}.vnp".format(i)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # print(tags)
    urll = []
    ori_url = "https://www.vietnamplus.vn/"
    for tag in tags:
        url = tag.get('href',None)
        if(url in urll):
            continue
        if(url == None):
            continue
        for i in range(9):
            if(('{}.vnp').format(i) in url):
                write_an_article(ori_url+url)
                urll.append(url)
                break
# with open("D:\Document\Python\crawl_data\\text.txt","a+") as ss:
#     ss.seek(0)
#     ss.write()