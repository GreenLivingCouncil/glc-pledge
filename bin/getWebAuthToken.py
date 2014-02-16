#!/usr/bin/python
from pledger import json_get_view, WebAuthToken

@json_get_view
def get_web_auth_token():
    return {
        "sunetId": WebAuthToken.sunet_id,
        "email"  : WebAuthToken.email,
        "name"   : WebAuthToken.name
        }
