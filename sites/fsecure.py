from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

fsecure_base = "https://blog.f-secure.com/whitepapers/"

def fsecure():
    print("Scraping FSecure")
    pageSoup = BeautifulSoup(requests.get(fsecure_base,headers=HEADERS).text, "lxml")
    docs = pageSoup.findAll("div",{"class" :"c-promo js-clickable"})
    for doc in docs:
        download_url = doc["data-url"]
        metadata = doc.find('p',{"class": "c-promo__text c-promo__text--2line"}).text
        file_download(download_url,"Whitepapers/FSecure/"+ doc.find("h3").text.strip(), download_url,metadata)
    print("Finished FSecure")