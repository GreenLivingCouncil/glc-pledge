#!/usr/bin/python
import pledger
import datetime

@pledger.json_post_view
def submit_pledge(pledge):
    if not pledger.submit_pledge(pledge):
        raise Exception

    return {
            "success" : True,
            "firstTime" : True
            }
