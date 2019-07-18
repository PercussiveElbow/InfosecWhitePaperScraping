from bs4 import BeautifulSoup
import requests,os
from time import sleep

# Headers
headers = {'User-Agent': "I'm scraping your whitepapers because they're good stuff ty xx"}

# Base URLs
mwr_base = "https://labs.mwrinfosecurity.com"
mdsec_base = "https://www.mdsec.co.uk"
spectreops_base = "https://specterops.io"
infosec_insitute_base = "https://www.infosecinstitute.com/white-papers/"
fsecure_base = "https://www.f-secure.com"

def mwr():
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
                file_download(mwr_base + file_link , "Whitepapers/MWR/" + dir_name ,file_link,metadata_text)
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
                        file_download(download_url,"Whitepapers/MDSec/" + title, download_url, metadata)
                sleep(5)
    print("Finished MDSec")

def infosec_insitute():
    print("Scraping InfoSecInstitute")
    pageSoup = BeautifulSoup(requests.get(infosec_insitute_base,headers=headers).text,"lxml")
    docs = pageSoup.findAll("a",{"class": "download-document"})
    for doc in docs:
        download_url = doc["href"]
        file_download(download_url,"Whitepapers/InfoSecInstitute/" +doc.find("h4").text[1:] ,download_url,doc.find("p").text)
        sleep(5)
    print("Finished InfoSecInstitute")

def fsecure():
    print("Scraping FSecure")
    pageSoup = BeautifulSoup(requests.get(fsecure_base + "/en/web/labs_global/whitepapers",headers=headers).text, "lxml")
    docs = pageSoup.findAll("div",{"class" :"p-t-xs-2 p-t-sm-2 text-center height-550 bg-white"})
    for doc in docs:
        #print(doc)
        download_url = doc.find("a",{"class": "btn btn-red"})["href"]
        if "www.f-secure.com" in download_url:
            download_url.replace("http://","https")
        else:
            download_url = fsecure_base + download_url
        metadata = ""
        if doc.find("p",{"class": "font-gray-5 p-y-xs-1 p-y-sm-1 text-small"}):
            metadata += doc.find("p",{"class": "font-gray-5 p-y-xs-1 p-y-sm-1 text-small"}).text + "\n"
        if doc.find("p",{"class": "tight p-b-xs-1 p-b-sm-1"}):
            metadata = doc.find("p",{"class": "tight p-b-xs-1 p-b-sm-1"}).text
        file_download(download_url,"Whitepapers/FSecure/"+ doc.find("h4").text, download_url,metadata)
        sleep(5)
    print("Finished InfoSecInstitute")

def spectreops():
    print("Scraping SpectreOps")
    pageSoup = BeautifulSoup(requests.get(spectreops_base + "/resources/research-and-development",headers=headers).text,"lxml")
    spectre_ops = pageSoup.find("div", {"class": "row justify-content-center"})

# probs need to use selenium here to avoid captchas blocking everything
def ncc():
    print()

## Generic methods below
def file_download(url, dir_name, file_name,metadata):
    make_dir(dir_name)
    print("Found article: " + dir_name)
    print("Downloading file from: " + url)
    file_name = file_name.replace("\\","").replace("..","")
    r = requests.get(url, allow_redirects=True,headers=headers)
    local_file_name = file_name.split("/")[-1]
    local_file_name.replace("..","").replace("/","")
    open(dir_name + "/" + local_file_name, 'wb').write(r.content)
    open(dir_name + "/" + "whitepaper_metadata","w").write(metadata)

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

## Scraping time
print("Beginning scraping: ")
mwr()
mdsec()
infosec_insitute()
fsecure()