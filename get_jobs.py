# Author: Daniel Zhao
# File: linkedin_get_jobs.py

# View database at http://dannizhao.iriscouch.com/_utils/index.html

import sys
import time
import couchdb
import httplib, json
from couchdb.design import ViewDefinition
from time import gmtime, strftime
from login import login

# Linkedin Industry Code: https://developer.linkedin.com/documents/industry-codes
# Industry: Retail
INDUSTRY_CODE = '68'
INDUSTRY_NAME = 'higher-education'

MAX_RESULTS = 5000
# Establish a connection to a CouchDB database

server = couchdb.Server('http://dannizhao.iriscouch.com/')
DB = 'linkedin-job-search-%s' % ( INDUSTRY_NAME, )
DB2 = 'linkedin-job-search-%s-response' % ( INDUSTRY_NAME, )

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

while start <= MAX_RESULTS:
	url = "http://api.linkedin.com/v1/job-search?facet=industry,"+ INDUSTRY_CODE +"&count=20&start="+ str(start) +"&format=json"
	resp, content = client.request(url)

# print resp
# print content

	db2.save( resp ) # This worked
	db.save( json.loads(content) )

	print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - collected 20 results'
	start += 20
