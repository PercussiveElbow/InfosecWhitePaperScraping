from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

symantec_base = "https://www.broadcom.com/support/security-center/publications/archive"

def symantec():
    print("Scraping Broadcom")
    pageSoup = BeautifulSoup(requests.get(symantec_base,headers=HEADERS).text,"lxml")
    whitepapers = pageSoup.find_all("div",{"class": "promo"})
    for whitepaper in whitepapers:
        print(whitepaper)
        download_url = whitepaper.find("a")["href"]
        download_title = whitepaper.find("a").text
        file_download(download_url,"Whitepapers/Broadcom/"+ download_title, download_url,"")
    print("Finished Broadcom")
