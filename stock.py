import re
import urllib.request
import urllib.parse



list=["indices/bse/sensex","indices/nse/cnx-nifty"]
main=[1,2]

l=(len(list))
for i in range(l):

    url="http://money.rediff.com/" + list[i] 

    try:
    
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5375.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
    except Exception as e:
        print(str(e))
    data = str(respData)
    source = re.findall(r'<span id="ltpid" class="f22">(.*?)</span>',data)
    

    main[i]=str(source[0])
  
   
    i=i+1


file = open('st.html','w')

file.write("""<html>
<head>
	<title>Stock</title>
	<link type="text/css" rel="stylesheet" href="stocks.css">
	
</head>


<body>
<a href="myhome.html"><div id="a1" class="tab">HOME</div></a>
<a href="st.html"><div id="a2" class="tab">STOCK MARKET</div></a>
<a href="sports.html"><div id="a3" class="tab">SPORTS</div></a>
<a href="world.html"><div id="a4" class="tab">WORLD</div></a>
<a href="tech.html"><div id="a5" class="tab">TECHNOLOGY</div></a>
<a href="index.html"><div id="a8" class="tab">SWITCH USER</div></a>
<a href="travel.html"><div id="a7" class="tab">TRAVEL</div></a>
<a href="entertainment.html"><div id="a6" class="tab">ENTERTAINMENT</div></a>



<div class="scroll-up">
	<p id="scroll">""")


url="http://www.24hgold.com/english/allmetalsdata.aspx?ms=1678642D5010"
try:
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5375.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    #print(respData)
except Exception as e:
    print(str(e))

data = str(respData)

gold = re.findall(r"""<td style="height:22px;width:140px;">Gold</td><td align="right" style="width:80px;">(.*?)</td>""",data)
silver = re.findall(r"""<td style="height:22px;width:140px;">Silver</td><td align="right" style="width:80px;">(.*?)</td>""",data)
plat = re.findall(r"""<td style="height:22px;width:140px;">Platinum</td><td align="right" style="width:80px;">(.*?)</td>""",data)
copper = re.findall(r"""<td style="height:22px;width:140px;">Copper Future</td><td align="right" style="width:80px;">(.*?)</td>""",data)
crude = re.findall(r"""<td style="height:22px;width:140px;">WTI Crude</td><td align="right" style="width:80px;">(.*?)</td>""",data)
gas = re.findall(r"""<td style="height:22px;width:140px;">Natural Gas</td><td align="right" style="width:80px;">(.*?)</td>""",data)

file.write("""	<span id="gold" class="txt">GOLD <br> """)
file.write(str(gold[0]))
file.write("""</span><br><br><br><br>""")
file.write("""	<span id="silver" class="txt">SILVER <br> """)
file.write(str(silver[0]))
file.write("""</span><br><br><br><br>""")
file.write("""	<span id="copper" class="txt">COPPER <br> """)
file.write(str(copper[0]))
file.write("""</span><br><br><br><br>""")
file.write("""	<span id="platinum" class="txt">PLATINUM <br> """)
file.write(str(plat[0]))
file.write("""</span><br><br><br><br>""")
file.write("""	<span id="crude" class="txt"> WTI CRUDE <br> """)
file.write(str(crude[0]))
file.write("""</span><br><br><br><br>""")
file.write("""	<span id="gas" class="txt">NATURAL GAS <br> """)
file.write(str(gas[0]))
file.write("""</span><br>""")
		


file.write("""	</p>
</div>

<div id="s1" class="stock"><span class="price">""")




file.write(str(main[0]))
file.write('</span><br><div class="name">BSE SENSEX</div> </div>')

file.write('<div id="s2" class="stock"><span class="price">')
file.write(str(main[1]))
file.write('</span><br><div class="name">BSE NIFTY</div></div>')

list=['tata-motors-ltd/20','icici-bank-ltd/6084','tata-consultancy-services-ltd/4126','reliance-industries-ltd/2877']
comp=[]

for i in range(len(list)):
    url="http://www.religareonline.com/company-fundamentals/" + list[i]
    a=open("abcd.html","w")
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('withHeaders.txt','w')
        saveFile.write(str(respData))
        saveFile.close()
    except Exception as e:
        print(str(e))

    data=str(respData)
    news=re.findall(r'<span id="CompanyHeader_div_ltp" class="s50 cGy3 ftPtSans lh40">(.*?)</span>',data)
    comp.append(news)
print(comp)

file.write("""<div id="s3" class="stock"><span class="price">""")
file.write(str(comp[0][0]))
file.write('</span><br><div class="name">TATA MOTORS LTD</div></div>')
file.write('<div id="s4" class="stock"><span class="price">')
file.write(str(comp[1][0]))
file.write('</span><br><div class="name">ICICI BANK LTD</div></div>')
file.write('<div id="s5" class="stock"><span class="price">')
file.write(str(comp[2][0]))
file.write('</span><br><div class="name">TCS LTD</div></div>')
file.write('<div id="s6" class="stock"><span class="price">')
file.write(str(comp[3][0]))
file.write("""</span><br><div class="name">RELIANCE</div></div>""")


url="http://www.indiainfoline.com/news-listing/top-news"
try:
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5375.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    #print(respData)
except Exception as e:
    print(str(e))

data = str(respData)
source = re.findall(r"""<p class="heading fs20e robo_slab mb10"><a href="/article/news-top-story/(.*?)</a></p>""",data)

news=[]
i=1
for a in source:
    a.split()
   

    b=a.split(">")
   
    if i<=10:
        news.append(b[1])
        i=i+1




file.write('<div id="n1" class="news">-')

file.write(str(news[0]))
file.write('</div>')

file.write('<div id="n2" class="news">-')

file.write(str(news[1]))
file.write('</div>')

file.write('<div id="n3" class="news">-')

file.write(str(news[2]))
file.write('</div>')

file.write('<div id="n4" class="news">-')

file.write(str(news[3]))
file.write('</div>')

file.write('<div id="n5" class="news">-')

file.write(str(news[4]))
file.write('</div>')

file.write('<div id="n6" class="news">-')

file.write(str(news[5]))
file.write('</div>')

file.write('<div id="n7" class="news">-')

file.write(str(news[6]))
file.write('</div>')

file.write('<div id="n8" class="news">-')

file.write(str(news[7]))
file.write('</div>')

file.write('<div id="n9" class="news">-')

file.write(str(news[8]))
file.write('</div>')

file.write('<div id="n10" class="news">-')

file.write(str(news[9]))
file.write('</div>')









company=[]
comp=['hdfc-bank-ltd/6082','itc-ltd/3916','infosys-ltd/4076','oil-and-natural-gas-corporation-ltd/2791','state-bank-of-india/6012','coal-india-ltd/9600']

for i in range(len(comp)):
    url="http://www.religareonline.com/company-fundamentals/" + comp[i]
   
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('withHeaders.txt','w')
        saveFile.write(str(respData))
        saveFile.close()
    except Exception as e:
        print(str(e))

    data=str(respData)
    news=re.findall(r'<span id="CompanyHeader_div_ltp" class="s50 cGy3 ftPtSans lh40">(.*?)</span>',data)
    company.append(news[0])
print(company)

file.write("""<marquee direction="right" speed="fast">""")
file.write("hdfc bank ltd : ")
file.write(company[0])
         
file.write("        ")
file.write("itc ltd : ")
file.write(company[1])
         
file.write("        ")
file.write("infosys ltd : ")
file.write(company[2])
         
file.write("        ")
file.write("ONGC ltd: ")
file.write(company[3])
         
file.write("        ")
file.write("SBI ltd : ")
file.write(company[4])
         
file.write("        ")
file.write("coal india ltd : ")
file.write(company[5])
"""         
file.write("        ")
file.write("hdfc bank ltd : ")
file.write(company[6])
         
file.write("        ")
file.write("hdfc bank ltd : ")
file.write(company[7])
         
file.write("        ")
file.write("hdfc bank ltd : ")
file.write(company[8])
         
file.write("        ")
file.write("hdfc bank ltd : ")
file.write(company[9])
"""
file.write('</marquee>')



file.write("""

</body>
</html>""")



file.close()


