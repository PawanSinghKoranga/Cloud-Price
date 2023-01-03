import asyncio
import requests
from bs4 import BeautifulSoup
import time
from forex_python.converter import CurrencyRates
c = CurrencyRates()

# url="https://aws.amazon.com/s3/pricing/"
url="https://www.apptio.com/blog/essential-guide-aws-s3-pricing/"

cval="h"
ccval=0
ctype="storage"
cdescription="S3 Glacier Deep Archive For long term data archiving that is accessed once or twice in a year and can be  ,per GB (Storage / Month)"
cprovider="AWS"

def fetch_data():
    r=requests.get(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent, 'html.parser')
    # print(soup)
    ele=soup.find_all('table')
    
    # print(ele[1].get_text())
    st=ele[1].get_text()
    # print(ele)
    
    # st=t.get_text()
    i=0
    # print(st)
    ctr=0
    for word in st:

        if(word=="$"): 
            ctr+=1

        if(word=="$" and ctr==16):
            break

            # nonlocal i
        
        i=i+1
        
    i+=1;
    pval=""

    # print(st[i+5])
    while(st[i]!="p"):
        pval+=st[i]
        i+=1
    print(pval)
        
    ival=float(pval)
    global ccval
    ccval = c.convert("USD","INR", ival)
    ccval=round(ccval,3)

    print(ccval)

                
        


# counter=0   

def upd():
    print("we are here")
    f = open("./subpro/obj15con.txt", "w")
    
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