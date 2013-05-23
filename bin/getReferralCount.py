#!/usr/bin/python
import sqlite3
import cgi
import json
# import cgitb
# cgitb.enable()

# TODO: provide the real name of the referrer

## Main script ##
form = cgi.FieldStorage()
# Open connection to sqlite db to get the referral count
conn = sqlite3.connect("pledges.db")
entry = conn.execute("select count from referralCounts where referrer=?", (form.getfirst("referrer"),) ).fetchone()
# Build response, fill in zero if entry does not exist yet for referrer
response = { "count" : 0 }
if entry:
    response["count"] = int(entry[0])
# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
