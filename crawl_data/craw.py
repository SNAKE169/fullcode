import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# url = "http://py4e-data.dr-chuck.net/known_by_Gil.html"
count = 4
pos = 3
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for i in range(4):
    number = 0
    for tag in tags:
        number += 1
        if(number == pos):
            url = tag.get('href',None)
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            if(i == 3):
                print(url)
            break
