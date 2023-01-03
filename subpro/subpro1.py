import asyncio
import requests
from bs4 import BeautifulSoup
import time
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://cloud.google.com/storage/"

cval="h"
ccval=0
ctype="storage"
cdescription="(per GB per month)STANDARD STORAGE"
cprovider="Google"
# clink="https://cloud.google.com/storage/"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    ele=soup.find(class_="pricing-module__table-cell")
    global cval
    cval=ele.get_text()
    fval=""
    starti=0
    for i, v in enumerate(cval):
        if(v=="$"):
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
    # print("here")
        
        

# counter=0   

def upd():
    print("we are here")
    f = open("./subpro/obj1con.txt", "w")
    # f.write("Hello world.")
    # global counter
    # counter+=1
    # f.write(str(counter))
    # f.write('\n')
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

        # with open('obj1con.txt', 'w') as f:
        
        #     f.write(str(ccval))
        #     f.write('\n')
        #     f.write(ctype)
        #     f.write('\n')
        #     f.write(cdescription)
        #     f.write('\n')
        #     f.write(cprovider)
        #     f.write('\n')
        #     f.write(url)
        #     f.write('\n')

        #     f.close()
        


async def main():
    while(1):
        # print("hum yaha he")
        # task1=asyncio.create_task(fetch_data())
        # task2=asyncio.create_task(upd())
        fetch_data()
        upd()
        time.sleep(1)
    # fval=""
    # starti=0
    # for i, v in enumerate(cval):
    #     if(v=="$"):
    #         starti=i
    #         break;
    # fval=cval[starti+1:]
    # ffval=""
    # for t in fval:
    #     if(t!=" "):
    #         ffval+=t
    #     else:
    #         break;
    # # print(ffval)
    # ccval=float(ffval)
    # print(ccval)



            
    # print(cdescription)
    
asyncio.run(main())