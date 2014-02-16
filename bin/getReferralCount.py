#!/usr/bin/python
import pledger

# TODO: provide the real name of the referrer

@pledger.json_get_view
def get_referral_count(referrer):
    return {
        "count" : pledger.get_referral_counts(referrer)
        }

