from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

mwr_base = "https://labs.mwrinfosecurity.com"

def mwr():
    print("Scraping MWR")
    for page in mwr_get_all_pages(mwr_base+"/archive/"):
        pageSoup = BeautifulSoup(requests.get(page,headers=HEADERS).text,"lxml")
        for articlePage in pageSoup.findAll("a", {"class": "col4 box-wrap"}):
            articleLink = articlePage['href']
            articleSoup = BeautifulSoup(requests.get(mwr_base + articleLink ,headers=HEADERS).text,"lxml")
            file_link = articleSoup.find("a", {"class": "box-wrap box-file"})
            if file_link:
                file_link = file_link["href"]
                title = articleSoup.find("h1").text
                author_date = articleSoup.find("strong").text
                dir_name = title.replace('\n', '').replace("\t", '') + "_" + author_date.replace('_', '').replace('\n', '').replace("\t", '')
                metadata_text=""
                for element in articleSoup.find("div",{"class": "blog-post"}).findAll('p'):
                    metadata_text += '\n' + ''.join(element.findAll(text = True))
                file_download(mwr_base + file_link , "Whitepapers/MWR/" + dir_name ,file_link,metadata_text)
    print("Finished scraping MWR")

def mwr_get_all_pages(link):
    pages = [link]
    while link != None:
        print("MWR: Current page scraped: " + link)
        parsed = BeautifulSoup(requests.get(link,headers=HEADERS).text, "lxml").find("a",{"class": "btn btn-next"})
        link = parsed["href"] if parsed else None 
        if link:
            link = mwr_base + "/" + link
            pages.append(link)
    return pages
