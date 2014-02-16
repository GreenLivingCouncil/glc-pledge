#!/usr/bin/python
import pledger

@pledger.json_get_view
def has_pledged(event_id):
    token = pledger.WebAuthToken
    return {
        "hasPledged": pledger.has_pledged(token.sunet_id, event_id)
        }
