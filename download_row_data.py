import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

# Setting URL WebPage
url = 'http://service.nso.go.th/nso/web/statseries/'
url_bkk = "http://service.nso.go.th/nso/web/statseries/tables/11000_Bangkok/12.5.1.xls"

page = urllib.request.urlopen(url+'statseries18.html')
soup = BeautifulSoup(page, "html.parser")
web_nav = soup.findAll('ul', {"class":"topnav"})[1]

# Names Region Thailand from weburl
region = {0:"ภาคกลาง", 1:"ภาคเหนือ", 2:"ภาคตะวันออกเฉียงเหนือ", 3:"ภาคใต้"}

# Start Loop for Downloading Xls Files
for x in region:
    d = web_nav.findAll('ul')[x]
    data = {i.text:url+i.get('href') for i in d.findAll('a')}
    print("--- > กำลังโหลดข้อมูลของ: "+region[x])
    if not os.path.exists("./rows_data/"+region[x]):
        os.makedirs("./rows_data/"+region[x])
    print("Downloading..  ")
    for i in data:
        # fix edit bad name this provice on nso web
        save = "ประจวบคีรีขันธ์" if i == "ประจวบคีรีขันธุ์" else i.strip()
        print(i, end=' ')
        urllib.request.urlretrieve(data[i], "./rows_data/"+region[x]+"/"+save+".xls")
        print("\tSuccess!!")

# Download Xls file Only Bangkok
urllib.request.urlretrieve(url_bkk, "./rows_data/ภาคกลาง/กรุงเทพมหานคร.xls")
print("Download: กรุงเทพมหานคร Success!!")

# Complete
print("===========All Download Complete")
