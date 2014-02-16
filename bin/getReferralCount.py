#!/usr/bin/python
import pledger

@pledger.json_get_view
def get_referral_count():
    referrer = pledger.WebAuthToken.sunet_id
    return {
        "count" : pledger.get_referral_counts(referrer)
        }

