import asyncio
import requests
from bs4 import BeautifulSoup
url="https://aws.amazon.com/ebs/?c=s&sec=srv"

r=requests.get(url)
htmlContent=r.content

soup=BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
print(soup.find(class_="lb-txt-28 lb-none-v-margin lb-rtxt").get_text())