#!/usr/bin/env python

# -*- coding: utf-8 -*- 
# Import extensible library for opening URLs
import urllib2, urllib

# Segment for translation
contentForTx  = "Acme Corp has the largest selection of dynamite and anvils on the market."

# The hostname of the project that contains the TM and OTX account
virtualHostName  = "es.acme.com"

# The hostname of the server the project is contained on
physicalHostName = "stagex1.onelink-translations.com"

# Set the parameters of the request, encode with url encoding.
params = urllib.urlencode({'otx_mimetype': 'text/html',
                           'otx_account' : 'acme,acmePassW0rd',
                           'otx_service' : 'tx',
                           'otx_content' : contentForTx})
# Set the host header
headers = {"Host": virtualHostName}

# Make the request object passing in the parameters and headers
req = urllib2.Request(b:: Content for translation    : Acme Corp has the largest selection of dynamite and anvils on the market.
:: Received translated content: Acme Corp tiene la mayor selecciC3n de dinamita y yunques en el mercado.
