from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

fsecure_base = "https://www.f-secure.com"

def fsecure():
    print("Scraping FSecure")
    pageSoup = BeautifulSoup(requests.get(fsecure_base + "/en/web/labs_global/whitepapers",headers=HEADERS).text, "lxml")
    docs = pageSoup.findAll("div",{"class" :"teaser-wrapper teaser--layout-box m-b-1"})
    for doc in docs:
        download_url = doc.find_all("a")[-1]["href"]
        download_url = fsecure_base + download_url
        metadata = ""
        if doc.find("p"):
            for paras in doc.findAll('p'):
                metadata += paras.text + "\n"
        file_download(download_url,"Whitepapers/FSecure/"+ doc.find("h3").text.strip(), download_url,metadata)
    print("Finished FSecure")