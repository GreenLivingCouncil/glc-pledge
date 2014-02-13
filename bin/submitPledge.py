#!/usr/bin/python
import sqlite3
import json
import cgi
import datetime
# import cgitb
# cgitb.enable()

## Helper Functions ##

def get_pledge():
    """Loads form data. Returns the data as a dict, or returns None if cannot parse JSON."""
    try:
        result = json.loads(cgi.FieldStorage().value)
        return result
    except (TypeError, ValueError):
        return None

def firstTimePledge(conn, pledge):
    """Returns True if it is first time that this user is pledging, and False otherwise."""
    #return True # uncomment this to allow multiple pledges per user
    return not bool(conn.execute("select * from pledges where sunetId=:sunetId and eventId=:eventId", pledge).fetchall())

def insertPledge(conn, pledge):
    """Inserts new pledge and increments team count and referral count."""
    conn.execute("insert into pledges (name, sunetId, email, teamId, eventId, dateString, comments, referrer, private) values (?,?,?,?,?,?,?,?,?)", (str(pledge['name']), str(pledge['sunetId']), str(pledge['email']), str(pledge['teamId']), str(pledge['eventId']), str(datetime.datetime.today()), str(pledge['comments']), str(pledge['referrer']), pledge['private']))

    # Create/increment team count
    if not conn.execute("select * from teamCounts where teamId=:teamId and eventId=:eventId", pledge).fetchall():
        conn.execute("insert into teamCounts (teamId, eventId) values (?,?)", (str(pledge['teamId']), str(pledge['eventId'])))
    conn.execute("update teamCounts set count=count+1 where teamId=:teamId and eventId=:eventId", pledge)
    
    # Increment referrer count if a referrer was specified
    if pledge['referrer']:
        # if the referrer is a valid sunetid of a previous pledger, go ahead and increment referral count
        if conn.execute("select * from pledges where sunetId=:referrer", pledge).fetchall():
            if not conn.execute("select * from referralCounts where referrer=:referrer", pledge).fetchall():
                conn.execute("insert into referralCounts (referrer) values (?)", (str(pledge['referrer']),)) # lazy instantiation
            conn.execute("update referralCounts set count=count+1 where referrer=:referrer", pledge)

    conn.commit()
    return True


## Main script ##

response = {}
form = getForm()
response["success"] = form is not None
# Open connection to sqlite db and attempt to insert new pledge
if response["success"]:
    conn = sqlite3.connect("pledges.db")
    response["firstTime"] = firstTimePledge(conn, form)
    if response["firstTime"]:
        response["success"] = insertPledge(conn, form)
# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
