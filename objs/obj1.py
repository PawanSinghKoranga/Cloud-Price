import asyncio
import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://cloud.google.com/storage/"

cval="h"
ccval=0
ctype="storage"
cdescription="STANDARD STORAGE"
cprovider="Google"
# clink="https://cloud.google.com/storage/"

async def fetch_data():
    while(1):
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
        
        await asyncio.sleep(10)
    
       




# async def main():
#     task1=asyncio.create_task(fetch_data())

#     # print("We are here")
#     await asyncio.sleep(2)
#     # fval=""
#     # starti=0
#     # for i, v in enumerate(cval):
#     #     if(v=="$"):
#     #         starti=i
#     #         break;
#     # fval=cval[starti+1:]
#     # ffval=""
#     # for t in fval:
#     #     if(t!=" "):
#     #         ffval+=t
#     #     else:
#     #         break;
#     # # print(ffval)
#     # ccval=float(ffval)
#     # print(ccval)



            
#     # print(cdescription)
    
# asyncio.run(main())