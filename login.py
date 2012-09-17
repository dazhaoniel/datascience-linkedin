# Author: Daniel Zhao
# File: linkedin_login.py

import oauth2 as oauth
import httplib2
import time, os, simplejson



def login():
	CONSUMER_KEY      =   'mtt4fefyssp5'
	CONSUMER_SECRET  =   'zz8tvRMUeYUn32vB'
	OAUTH_TOKEN           =   '53e42f02-8009-4c9e-8c1d-82a98b6b50f2'
	OAUTH_TOKEN_SECRET          =   'df69d1b1-2831-42f0-bd86-c565150e460d'

	url = "http://api.linkedin.com/v1/people/~?format=json"

	consumer = oauth.Consumer(
     		key= CONSUMER_KEY,
     		secret= CONSUMER_SECRET )
     
	token = oauth.Token(
     		key= OAUTH_TOKEN, 
     		secret= OAUTH_TOKEN_SECRET )


	client = oauth.Client(consumer, token)

	resp, content = client.request(url)

	#print resp
	#print content
	return client

if __name__ == '__main__':
	login()
