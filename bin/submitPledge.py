#!/usr/bin/python
import cgi
import json
import pledger
import datetime

def get_pledge():
    """Loads form data. Returns the data as a dict, or returns None if cannot parse JSON."""
    try:
        pledge = json.loads(cgi.FieldStorage().value)
        pledge['dateString'] = str(datetime.datetime.today())
        if not pledger.is_valid_pledge_dict(pledge):
            raise ValueError
        return pledge
    except (TypeError, ValueError):
        return None

pledge = get_pledge()
success = pledge is not None
first_time = pledger.is_first_pledge(pledge)
if success and first_time:
    success = pledger.submit_pledge(pledge)
response = {
        "success" : success,
        "firstTime" : first_time
        }

# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
