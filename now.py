import re
import urllib.request
import urllib.parse



file = open('stocks.txt','w')

url="http://money.rediff.com/indices/bse/sensex?srchword=BSE+Sensex&snssrc=sugg" 

try:
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5375.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
       

    
except Exception as e:
    print(str(e))

    
data = str(respData)
source = re.findall(r'<div id="div_global">(.*?)<div id="div_domestic"',data)
   
print(source)
  
file.close()
