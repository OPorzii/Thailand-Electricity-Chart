import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

theurl = 'http://service.nso.go.th/nso/web/statseries/statseries18.html'
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

web_nav = soup.findAll('ul', {"class":"topnav"})[1]
con = {0:"ภาคกลาง", 1:"ภาคเหนือ"}
for x in con:
    d = web_nav.findAll('ul')[x]
    data = {}
    for i in d.findAll('a'):
        data[i.text] = 'http://service.nso.go.th/nso/web/statseries/'+i.get('href')
    print("กำลังโหลดข้อมูล: "+con[x])
    if not os.path.exists("./_RowData/"+con[x]):
        os.makedirs("./_RowData/"+con[x])
    for i in data:
        print("Downloading..  "+i, end='')
        urllib.request.urlretrieve(data[i], "./_RowData/"+con[x]+"/"+i+".xls")
        print("\tSuccess!!")

print("Download Complete")
