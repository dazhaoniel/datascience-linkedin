# Author: Daniel Zhao
# File: linkedin_get_jobs.py

# View database at http://localhost:5984/_utils/index.html

import sys
import time
import couchdb
import httplib, json
from couchdb.design import ViewDefinition
from login import login

# Linkedin Industry Code: https://developer.linkedin.com/documents/industry-codes
# Industry: Information Technology and Services
INDUSTRY_CODE = '96'

MAX_RESULTS = 5000
# Establish a connection to a CouchDB database

server = couchdb.Server('http://localhost:5984')
DB = 'job-postings-%s' % ( INDUSTRY_CODE, )


try:
	db = server.create(DB)
except couchdb.http.PreconditionFailed, e:

	# Already exists, so append to it, keeping in mind that duplicates could occur
	db = server[DB]



client = login()
start = 0
# url = "http://api.linkedin.com/v1/people/~?format=json"

while start <= MAX_RESULTS:
	url2 = "http://api.linkedin.com/v1/job-search?facet=industry,"+ INDUSTRY_CODE +"&count=20&start="+ str(start) +"&format=json"
	resp, content = client.request(url2)

#print resp
#print content
#for row in content
#	db.save(row)

#db.save(resp) # This worked
	db.save( json.loads(content) )
	start += 20
