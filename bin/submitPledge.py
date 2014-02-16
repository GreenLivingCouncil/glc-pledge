#!/usr/bin/python
import pledger
import datetime

@pledger.json_post_view
def submit_pledge(pledge):
    first_time = not pledger.has_pledged(pledge['sunetId'], pledge['eventId'])
    if first_time and not pledger.submit_pledge(pledge):
        raise Exception

    return {
            "success" : True,
            "firstTime" : first_time
            }
