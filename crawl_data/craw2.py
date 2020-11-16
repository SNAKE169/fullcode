from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_887738.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('td')
ans = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('class', None))
    #ans = ans + int(tag.contents[0]) 
    print('Contents 0 :', tag.contents[0])
    # print('Contents 1 :', tag.contents[1])
    print('Attrs:', tag.attrs)