#!/usr/bin/env python
# -*- coding: utf-8 -*- # Import extensible library for opening URLs
import urllib2, urllib
# Segment for translation
contentForTx = "Acme Corp has the largest selection of dynamite and anvils on the market."
# The hostname of the project that contains the TM and OTX account
virtualHostName = "es-otx.onelink-poc.com"
# The hostname of the server the project is contained on
physicalHostName = "es-otx.onelink-poc.com"
# Set the parameters of the request, encode with url encoding.
params = urllib.urlencode({'otx_mimetype': 'text/html',
 'otx_account' : 'otx,otxpass', 'otx_service' : 'wmt', 'otx_content' : contentForTx})
# Set the host header
headers = {"Host": virtualHostName}
# Make the request object passing in the parameters and headers
req = urllib2.Request("https://"+physicalHostName+"/OneLinkOTX/", params, headers)
# Execute the request
response = urllib2.urlopen(req)
# Read the response
htmlData = response.read()
print ":: Content for translation : "+contentForTx
print ":: Received translated content: "+htmlData
