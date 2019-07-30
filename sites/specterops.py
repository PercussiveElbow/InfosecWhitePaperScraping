from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

spectreops_base = "https://specterops.io"

def spectreops():
    print("Scraping SpectreOps")
    pageSoup = BeautifulSoup(requests.get(spectreops_base + "/resources/research-and-development",headers=HEADERS).text,"lxml")
    spectre_ops = pageSoup.find("div", {"class": "row justify-content-center"})
