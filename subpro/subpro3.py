import asyncio
import requests
import time
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://cloud.google.com/storage/"

cval="h"
ccval=0
ctype="storage"
cdescription="NEARLINE STORAGE(per GB per month))"
cprovider="Google"
# clink="https://cloud.google.com/storage/"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.find_all("p", class_="lead"))
    # print(soup.find_all(class_="pricing-module__table-cell"))
    ele=soup.find_all(class_="pricing-module__table-cell")

    ele=ele[1]
    # print(ele)
    global cval
    cval=ele.get_text()
    # print(cval)
    fval=""
    starti=0
    for i, v in enumerate(cval):
        if(v=="$" ):
            starti=i
            break;
                
    fval=cval[starti+1:]
    ffval=""
    for t in fval:
        if(t!=" "):
            ffval+=t
        else:
            break;
    # print(ffval)
    global ccval
    ccval=float(ffval)
    ccval = c.convert("USD","INR", ccval)
    ccval=round(ccval,3)
    # print(ccval)
        
    # await asyncio.sleep(10)



def upd():
    print("we are here")
    f = open("./subpro/obj3con.txt", "w")
    
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