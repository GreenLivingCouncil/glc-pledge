#!/usr/bin/python
import sqlite3
import cgi
import datetime
import json
# import cgitb
# cgitb.enable()

# the naming of the 'data' field is unfortunate.. TODO change it to 'pledges' eventually

## Main script ##
form = cgi.FieldStorage()
# Open connection to sqlite db and pull the recent pledges
conn = sqlite3.connect("pledges.db")
pledges = conn.execute("select name, teamId, dateString, comments, private from pledges "
        "where eventId=:eventId order by dateString desc limit :limitSize", 
        {"eventId": form.getfirst("eventId"), "limitSize": form.getfirst("limit","10")}).fetchall()
# Generate JSON response
response = {
        "pledges" : []
        }
for pledge in pledges:
    pledgeTime = datetime.datetime.strptime(pledge[2], '%Y-%m-%d %H:%M:%S.%f')
    td = datetime.datetime.today() - pledgeTime
    hoursAgo = (td.seconds/3600) + td.days * 24
    if (int(pledge[4])):
        dispName = "Anonymous"
    else:
        dispName = pledge[0]
    response["pledges"].append({
        "name": dispName,
        "teamId": pledge[1],
        "hoursAgo": hoursAgo,
        "comments": pledge[3]
        })
print "Content-Type: application/json"
print
print json.dumps(response, indent=4, separators=(',', ': '))
