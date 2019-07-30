import os, requests

HEADERS = {'User-Agent': "I'm scraping your whitepapers because they're good stuff ty xx"}

## Generic methods below
def file_download(url, dir_name, file_name,metadata):
    make_dir(dir_name)
    print("Found article: " + dir_name)
    print("Downloading file from: " + url)
    file_name = file_name.replace("\\","").replace("..","")
    r = requests.get(url, allow_redirects=True,headers=HEADERS)
    local_file_name = file_name.split("/")[-1]
    local_file_name.replace("..","").replace("/","")
    open(dir_name + "/" + local_file_name, 'wb').write(r.content)
    open(dir_name + "/" + "whitepaper_metadata","w").write(metadata)

def make_dir(directory):
    directory = directory.replace("\\"," ")
    if not os.path.exists(directory):
        os.makedirs(directory)