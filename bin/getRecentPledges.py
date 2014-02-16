#!/usr/bin/python
import pledger

@pledger.json_get_view
def get_recent_pledges(event_id, limit=10):
    return {
        "pledges" : pledger.get_pledges(event_id, limit)
        }
