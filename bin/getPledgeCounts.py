#!/usr/bin/python
import pledger

@pledger.json_get_view
def get_pledge_counts(event_id):
    return pledger.get_pledge_counts(event_id)
