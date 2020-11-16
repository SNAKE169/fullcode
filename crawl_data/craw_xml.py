import urllib.request, urllib.parse, urllib.error

import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_887740.xml"

data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)
ls = tree.findall('comments/comment')

ans = 0
for item in ls:
    ans = ans + int(item.find('count').text)
    print(item.find('count').text)
print(ans)
