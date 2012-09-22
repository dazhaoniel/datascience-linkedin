# Author: Daniel Zhao
# File: linkedin_get_company_new_hires.py

# View database at http://localhost:5984/_utils/index.html

import sys
import time
import couchdb
import httplib, json
from couchdb.design import ViewDefinition
from time import gmtime, strftime
from login import login

# Linkedin Industry Code: https://developer.linkedin.com/documents/industry-codes
# Industry: Retail
COMPANY_NAME = 'aramark'
COMPANY_CODE = '2815'

FILE_NAME = 'response/company-%s-new-hires.xml' % ( COMPANY_NAME, )

client = login()

url = "https://api.linkedin.com/v1/companies/"+ COMPANY_CODE +"/updates?event-type=new-hire&count=20&start=0" 
resp, content = client.request(url)

# print resp
# print content
f = open(FILE_NAME, "wb")
f.write( content )
f.close()
