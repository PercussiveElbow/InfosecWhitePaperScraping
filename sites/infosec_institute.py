from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

infosec_insitute_base = "https://www.infosecinstitute.com/white-papers/"

def infosec_insitute():
    print("Scraping InfoSecInstitute")
    pageSoup = BeautifulSoup(requests.get(infosec_insitute_base,headers=HEADERS).text,"lxml")
    docs = pageSoup.findAll("a",{"class": "infosec-library-card-wrapper"})
    for doc in docs:
        download_page_url = doc["href"] + "?utm_status=success"  # z0mg leet 0 day bypass no addy required ;OOOO  
        downloadPageSoup = BeautifulSoup(requests.get(download_page_url,headers=HEADERS).text,"lxml")
        print(download_page_url)
        download_url = downloadPageSoup.find("div", {"class": "infosec-form-success-button-wrapper"}).find("a")["href"]
        file_download(download_url,"Whitepapers/InfoSecInstitute/" +doc.find("h3").text[1:] ,download_url,"")
    print("Finished InfoSecInstitute")