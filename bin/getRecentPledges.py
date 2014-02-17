#!/usr/bin/python
import pledger
import datetime

def make_pledge_dict(entry):
    """
    Given a single SQL namedtuple from the pledge table,
    return a dict with the display name, team ID, hours elapsed, and comments.
    """
    pledge_time = datetime.datetime.strptime(entry.dateString, '%Y-%m-%d %H:%M:%S.%f')

    return {
        "name": "Anonymous" if entry.private else entry.name,
        "teamId": entry.teamId,
        "isoDateString": pledge_time.isoformat(),
        "comments": entry.comments
        }

@pledger.json_get_view
def get_recent_pledges(event_id, limit=10):
    pledges = pledger.get_pledges(event_id, limit)
    pledge_dicts = [make_pledge_dict(pledge) for pledge in pledges]

    return {
        "pledges" : pledge_dicts
        }
