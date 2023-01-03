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
cdescription="COLDLINE STORAGE ,per GB per Month"
cprovider="Google"
# clink="https://cloud.google.com/storage/"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.find_all("p", class_="lead"))
    # print(soup.find_all(class_="pricing-module__table-cell"))
    ele=soup.find_all(class_="pricing-module__table-cell")

    ele=ele[2]
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
    # print(fval)
    ffval=""
    for t in fval:
        # print(t)
        if(t=='.' or (t>="0" and t<="9" )):
            ffval+=t
        else:
            break;
    # print(ffval)
    global ccval
    ccval=float(ffval)
    ccval = c.convert("USD","INR", ccval)
    ccval=round(ccval,3)
    # print(ccval)
        
def upd():
    print("we are here")
    f = open("./subpro/obj16con.txt", "w")
    
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

fetch_data()
    