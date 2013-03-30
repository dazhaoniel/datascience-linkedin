# Author: Daniel Zhao
# File: linkedin_login.py

import oauth2 as oauth
import httplib2
import time, os, simplejson



def login():
	CONSUMER_KEY      =   ''
	CONSUMER_SECRET  =   ''
	OAUTH_TOKEN           =   ''
	OAUTH_TOKEN_SECRET          =   ''

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
