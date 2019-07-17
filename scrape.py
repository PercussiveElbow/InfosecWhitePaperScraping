from bs4 import BeautifulSoup
import requests,os
from time import sleep

# Headers
headers = {'User-Agent': "I'm scraping your whitepapers because they're good stuff ty xx"}

# Base URLs
mwr_base = "https://labs.mwrinfosecurity.com"
mdsec_base = "https://www.mdsec.co.uk"

def mwr():
    make_dir("mwr")
    print("Scraping MWR")
    for page in mwr_get_all_pages(mwr_base+"/publications/"):
        pageSoup = BeautifulSoup(requests.get(page,headers=headers).text,"lxml")
        for articlePage in pageSoup.findAll("a", {"class": "col4 box-wrap"}):
            articleLink = articlePage['href']
            articleSoup = BeautifulSoup(requests.get(mwr_base + articleLink ,headers=headers).text,"lxml")
            file_link = articleSoup.find("a", {"class": "box-wrap box-file"})
            if file_link:
                file_link = file_link["href"]
                title = articleSoup.find("h1").text
                author_date = articleSoup.find("strong").text
                dir_name = title.replace('\n', '').replace("\t", '') + "_" + author_date.replace('_', '').replace('\n', '').replace("\t", '')
                metadata_text=""
                for element in articleSoup.find("div",{"class": "blog-post"}).findAll('p'):
                    metadata_text += '\n' + ''.join(element.findAll(text = True))
                file_download(mwr_base + file_link , "mwr/" + dir_name ,file_link,metadata_text)
            sleep(5) # Being polite
    print("Finished scraping MWR")

def mwr_get_all_pages(link):
    pages = [link]
    while link != None:
        print("MWR: Current page scraped: " + link)
        parsed = BeautifulSoup(requests.get(link,headers=headers).text, "lxml").find("a",{"class": "btn btn-next"})
        link = parsed["href"] if parsed else None 
        if link:
            link = mwr_base + "/" + link
            pages.append(link)
    return pages

def mdsec():
    print("Scraping MDSec")
    pageSoup = BeautifulSoup(requests.get(mdsec_base + "/research",headers=headers).text,"lxml")
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
                        file_download(download_url,"mdsec/" + title, download_url, metadata)
                sleep(5)
    print("Finished MDSec")

# probs need to use selenium here to avoid captchas blocking everything
def ncc():
    print()

## Generic methods below
def file_download(url, dir_name, file_name,metadata):
    make_dir(dir_name)
    print("Found article: " + dir_name)
    print("Found file link: " + url)
    file_name = file_name.replace("\\","").replace("..","")
    r = requests.get(url, allow_redirects=True,headers=headers)
    local_file_name = file_name.split("/")[-1]
    open(dir_name + "/" + local_file_name, 'wb').write(r.content)
    open(dir_name + "/" + "whitepaper_metadata","w").write(metadata)

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

## Scraping time
mwr()
mdsec()