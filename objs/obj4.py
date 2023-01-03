import asyncio
import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates
c = CurrencyRates()

url="https://cloud.google.com/storage/"

cval="h"
ccval=0
ctype="storage"
cdescription="ARCHIVE STORAGE"
cprovider="Google"
# clink="https://cloud.google.com/storage/"

async def fetch_data():
    while(1):
        r=requests.get(url)
        htmlContent=r.content
        soup=BeautifulSoup(htmlContent, 'html.parser')
        # print(soup.find_all("p", class_="lead"))
        # print(soup.find_all(class_="pricing-module__table-cell"))
        ele=soup.find_all(class_="pricing-module__table-cell")

        ele=ele[3]
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