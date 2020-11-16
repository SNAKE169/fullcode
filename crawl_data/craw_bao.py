from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://www.vietnamplus.vn/hai-duong-nang-chat-luong-sinh-hoat-chi-bo-gan-voi-nhiem-vu-chinh-tri/657850.vnp"
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find("div",{"class":"content article-body cms-body"})
print(tags('p'))