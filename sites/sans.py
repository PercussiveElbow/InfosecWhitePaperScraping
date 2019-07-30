from bs4 import BeautifulSoup
import requests,os,time
from sites.helper.help_utils import *

# Base URLs
sans_pentest_base = "https://pen-testing.sans.org"

def sans():
    print("Scraping SANS")
    pageSoup = BeautifulSoup(requests.get(sans_pentest_base + "/resources/whitepapers",headers=HEADERS).text, "lxml")
    docs = pageSoup.findAll("table",{"class" :"clear"})
    for doc in docs:
        rows = doc.find_all("tr", {"class" : "table-row"})
        rows_alt = doc.find_all("tr", {"class" : "table-row-alt"})
        all_rows = rows + rows_alt
        for row in all_rows:
            download_url = row.find("a")["href"]
            download_url = sans_pentest_base + download_url
            title = row.find("a").text
            metadata = ""
            if row.find("td",{"class": "table_data table_data_name"}):
                metadata += row.find("td",{"class": "table_data table_data_name"}).text + "\n"
            file_download(download_url,"Whitepapers/SANS/" + title , download_url,metadata)
            time.sleep(5)
    print("Finished SANS")
