#!/usr/bin/python
import cgi
import json
import pledge

form = cgi.FieldStorage()
event_id = form.getfirst("eventId")
response = pledge.get_pledge_counts(event_id)

# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
