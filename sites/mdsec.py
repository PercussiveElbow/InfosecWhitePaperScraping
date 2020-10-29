from bs4 import BeautifulSoup
import requests,os,time,git
from sites.helper.help_utils import *


def mdsec():
    print("Cloning MDSec research")
    make_dir("Whitepapers/MDSec",depth=1)
    git.Git("Whitepapers/MDSec/").clone("https://github.com/mdsecresearch/Publications.git")
    
    print("Finished MDSec")
