import asyncio
import requests
from bs4 import BeautifulSoup
import time
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://azure.microsoft.com/en-in/pricing/"

cval="h"
ccval=0
ctype="storage"
cdescription="Block Blob storage (ZRS HOT)/per GB per month"
cprovider="Azure"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    # print(soup)
    ele=soup.find_all(class_="price-value")
    # print(ele.get_text())
    ctr=0
    for t in ele:
        if(ctr==2):
            s=t.get_text()
            s=s[1:]
            # print(s)
            global ccval
            ccval=float(s)
            ccval = c.convert("USD","INR", ccval)
            ccval=round(ccval,3)
            break;
        # print(t.get_text())
        ctr+=1


# counter=0   

def upd():
    print("we are here")
    f = open("./subpro/obj4con.txt", "w")
    
    # global counter
    # counter+=1
    
    
    # global ccval
    # ccval+=counter
    f.write(str(ccval))
    f.write('\n')
    f.write(ctype)
    f.write('\n')
    f.write(cdescription)
    f.write('\n')
    f.write(cprovider)
    f.write('\n')
    f.write(url)
    f.write('\n')
    f.close()



async def main():
    while(1):
        fetch_data()
        upd()
        time.sleep(1)
    



    
asyncio.run(main())