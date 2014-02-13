#!/usr/bin/python
import cgi
import datetime
import json
import pledge

form = cgi.FieldStorage()
event_id = form.getfirst("eventId")
max_pledges = form.getfirst("limit", "10")
response = {"pledges" : pledge.get_pledges(event_id, max_pledges)}

print "Content-Type: application/json"
print
print json.dumps(response, indent=4, separators=(',', ': '))
