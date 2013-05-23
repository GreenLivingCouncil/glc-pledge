#!/usr/bin/python
import sqlite3
import cgi
import json
# import cgitb
# cgitb.enable()

## Main script ##
form = cgi.FieldStorage()
# Open connection to sqlite db and do the whole shebang
conn = sqlite3.connect("pledges.db")
result = dict(conn.execute("select teamId, count from teamCounts where eventId=:eventId", form.getfirst("eventId")).fetchall())
# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
