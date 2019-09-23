from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

mdsec_base = "https://www.mdsec.co.uk"

def mdsec():
    print("Scraping MDSec")
    pageSoup = BeautifulSoup(requests.get(mdsec_base + "/research",headers=HEADERS).text,"lxml")
    sections = pageSoup.find("div",{"class":"accordion"}).findAll("h3")
    if sections:
        for section in sections:
            if section.text == "Whitepapers" or section.text == "Presentations":
                papers = section.next_sibling.findAll("p")
                for paper in papers:
                    title = paper.find("strong")
                    if title:
                        title = title.text
                        download_url = paper.next_sibling("a")[0]["href"]
                        if download_url[0] == "/":
                            download_url = mdsec_base + download_url
                        if "github.com" in download_url:
                            download_url = download_url.replace("github.com","raw.githubusercontent.com").replace("/blob","")
                        metadata = ""
                        # if paper.next_sibling:
                        #     print("Next sibling: s" + paper.next_sibling.find("p")
                        file_download(download_url,"Whitepapers/MDSec/" + title, download_url, metadata)
    print("Finished MDSec")
