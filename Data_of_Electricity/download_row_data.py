import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

# Setting URL WebPage
url = 'http://service.nso.go.th/nso/web/statseries/'

page = urllib.request.urlopen(url+'statseries18.html')
soup = BeautifulSoup(page, "html.parser")
web_nav = soup.findAll('ul', {"class":"topnav"})[1]

# Names Region Thailand from weburl
region = {0:"ภาคกลาง", 1:"ภาคเหนือ"}

# Start Loop for Downloading Xls File
for x in region:
    d = web_nav.findAll('ul')[x]
    data = {i.text:url+i.get('href') for i in d.findAll('a')}
    print("--- > กำลังโหลดข้อมูลของ: "+region[x])
    if not os.path.exists("./_RowData/"+region[x]):
        os.makedirs("./_RowData/"+region[x])
    print("Downloading..  ")
    for i in data:
        print(i, end=' ')
        urllib.request.urlretrieve(data[i], "./_RowData/"+region[x]+"/"+i+".xls")
        print("\tSuccess!!")

# Complete
print("===========All Download Complete")
