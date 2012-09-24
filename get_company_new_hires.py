# Author: Daniel Zhao
# File: linkedin_get_company_new_hires.py

# View database at http://dannizhao.iriscouch.com/

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
'''
FILE_NAME = 'response/company-%s-new-hires.xml' % ( COMPANY_NAME, )

client = login()

url = "https://api.linkedin.com/v1/companies/"+ COMPANY_CODE +"/updates?event-type=new-hire&count=20&start=0" 
resp, content = client.request(url)

# print resp
# print content
f = open(FILE_NAME, "wb")
f.write( content )
f.close()
'''


# Establish a connection to a CouchDB database

server = couchdb.Server('http://dannizhao.iriscouch.com/')
DB = 'company-%s-new-hires' % ( COMPANY_NAME, )
DB2 = 'company-%s-new-hires-meta' % ( COMPANY_NAME, )

try:
	db = server.create(DB)
except couchdb.http.PreconditionFailed, e:

	# Already exists, so append to it, keeping in mind that duplicates could occur
	db = server[DB]

try:
	db2 = server.create(DB2)
except couchdb.http.PreconditionFailed, e:

	# Already exists, so append to it, keeping in mind that duplicates could occur
	db2 = server[DB2]


client = login()
start = 0


url = "https://api.linkedin.com/v1/companies/"+ COMPANY_CODE +"/updates?event-type=new-hire&count=20&start="+ str(start) +"&format=json"
resp, content = client.request(url)

# print resp
# print content

db2.save( resp ) # This worked
db.save( json.loads(content) )

# print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - collected 20 results'
# start += 20
