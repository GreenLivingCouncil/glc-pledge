#!/usr/bin/python
import cgi
import os
import json
# import cgitb
# cgitb.enable()

# Build collect WebAuth login info from environment variables
response = {
        "sunetId": os.environ['WEBAUTH_USER'],
        "email": os.environ['WEBAUTH_LDAP_MAIL'],
        "name": os.environ['WEBAUTH_LDAP_DISPLAYNAME']
        }

# Emit JSON message
print "Content-Type:application/json"
print 
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
