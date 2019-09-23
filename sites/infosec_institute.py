from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

infosec_insitute_base = "https://www.infosecinstitute.com/white-papers/"

def infosec_insitute():
    print("Scraping InfoSecInstitute")
    pageSoup = BeautifulSoup(requests.get(infosec_insitute_base,headers=HEADERS).text,"lxml")
    docs = pageSoup.findAll("a",{"class": "download-document"})
    for doc in docs:
        download_url = doc["href"]
        file_download(download_url,"Whitepapers/InfoSecInstitute/" +doc.find("h4").text[1:] ,download_url,doc.find("p").text)
    print("Finished InfoSecInstitute")