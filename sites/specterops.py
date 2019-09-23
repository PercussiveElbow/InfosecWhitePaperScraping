from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

specterops_base = "https://specterops.io"

def specterops():
    print("Scraping SpectreOps")
    pageSoup = BeautifulSoup(requests.get(specterops_base + "/resources/research-and-development",headers=HEADERS).text,"lxml")
    ebooks = pageSoup.find_all("div",{"class": "ebook"})
    for ebook in ebooks:
        download_url = ebook.find("a",{"class": "ebook__actions"})["href"]
        download_title = ebook.find("h5",{"class":"ebook__title"}).text
        file_download(specterops_base + download_url,"Whitepapers/SpectreOps/"+ download_title, download_url,"")
    print("Finished SpectreOps")
