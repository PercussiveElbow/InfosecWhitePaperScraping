from sites.fsecure_labs import *
from sites.mdsec import *
from sites.infosec_institute import *
from sites.fsecure import *
from sites.specterops import *
from sites.sans import *
from sites.symantec import *

## Scraping time
print("Beginning scraping: ")
fsecure_labs()
mdsec()
#infosec_insitute() borked
fsecure()
specterops()
sans()
#symantec() borked
