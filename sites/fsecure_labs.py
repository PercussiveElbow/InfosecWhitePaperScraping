from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

fsecure_labs_base = "https://labs.f-secure.com"

def fsecure_labs():
    print("Scraping F-Secure Labs")
    for page in fsecure_labs_get_all_pages(fsecure_labs_base+"/archive/"):
        pageSoup = BeautifulSoup(requests.get(page,headers=HEADERS).text,"lxml")
        for articlePage in pageSoup.findAll("a", {"class": "col4 box-wrap"}):
            articleLink = articlePage['href']
            articleSoup = BeautifulSoup(requests.get(fsecure_labs_base + articleLink ,headers=HEADERS).text,"lxml")
            file_link = articleSoup.find("a", {"class": "flex-container__box"})
            if file_link:
                file_link = file_link["href"]
                title = articleSoup.find("h1").text
                author_date = articleSoup.find("p",{"class": "blog-post-meta"}).text
                dir_name = title.replace('\n', '').replace("\t", '') + "_" + author_date.replace('_', '').replace('\n', '').replace("\t", '')
                metadata_text=""
                for element in articleSoup.find("div",{"class": "blog-post"}).findAll('p'):
                    metadata_text += '\n' + ''.join(element.findAll(text = True))
                file_download(fsecure_labs_base + file_link , "Whitepapers/FSecureLabs/" + dir_name ,file_link,metadata_text)
    print("Finished scraping F-Secure Labs")

def fsecure_labs_get_all_pages(link):
    pages = [link]
    while link != None:
        print("FSecure-Labs: Current page scraped: " + link)
        parsed = BeautifulSoup(requests.get(link,headers=HEADERS).text, "lxml").find("a",{"class": "btn btn-next"})
        link = parsed["href"] if parsed else None 
        if link:
            link = fsecure_labs_base + "/" + link
            pages.append(link)
    return pages
