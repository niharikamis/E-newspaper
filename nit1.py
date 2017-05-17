import re
import urllib.request
import urllib.parse
url='http://timesofindia.indiatimes.com'
a=open("headline.html","w")
try:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

a.write("<html><head></head><body><p>")
print("latest news")
data=str(respData)
news=re.findall(r'<ul data-vr-zone="latest" class="list9">(.*?)</ul>',data)
d=news[0].split("title=")
for i in d:
    if ("href" in i):
        b=i.split("href")[0]
        print(b)
        a.write(b)
        a.write("<br>")
a.write("</body></html>")
a.close()
