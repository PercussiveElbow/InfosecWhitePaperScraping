import os,requests,re,time

HEADERS = {'User-Agent': "I'm scraping your whitepapers because they're good stuff ty xx"}

## Generic methods below
def file_download(url, dir_name, file_name,metadata):
    dir_name = sanitize(dir_name)
    file_name = sanitize(file_name)
    make_dir(dir_name)
    print("Found whitepaper: " + file_name)
    print("Downloading file: " + url)
    r = requests.get(url, allow_redirects=True,headers=HEADERS)
    local_file_name = file_name.split("/")[-1]
    local_file_name.replace("..","").replace("/","")
    open(dir_name + "/" + local_file_name, 'wb').write(r.content)
    open(dir_name + "/" + "whitepaper_metadata","w").write(metadata)
    time.sleep(5)

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize(unsanitized):
    # return unsanitized.replace("\\"," ").replace(":"," ").replace("..","").replace("").replace(","," ").replace("|", " ").replace("="," ").replace("[")
    sanitized =  re.sub('[;|:|\||\\|,|[|\]|"|*|?]|<|>', ' ', unsanitized)
    return re.sub('\s+', ' ', sanitized      ).strip()
