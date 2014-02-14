#!/usr/bin/python
import cgi
import datetime
import json
import pledger

form = cgi.FieldStorage()
event_id = form.getfirst("eventId")
max_pledges = form.getfirst("limit", "10")
response = {
        "pledges" : pledger.get_pledges(event_id, max_pledges)
        }

print "Content-Type: application/json"
print
print json.dumps(response, indent=4, separators=(',', ': '))
