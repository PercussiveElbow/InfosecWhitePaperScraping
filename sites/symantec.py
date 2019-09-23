from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

symantec_base = "https://www.symantec.com/"

def symantec():
    print("Scraping Symantec")
    pageSoup = BeautifulSoup(requests.get(symantec_base + "security-center/white-papers",headers=HEADERS).text,"lxml")
    whitepapers = pageSoup.find_all("span",{"class": "symantecBlueBullet"})
    for whitepaper in whitepapers:
        download_url = whitepaper.find("a")["href"]
        download_title = whitepaper.find("a").text
        file_download(symantec_base + download_url,"Whitepapers/Symantec/"+ download_title, download_url,"")
    print("Finished Symantec")
