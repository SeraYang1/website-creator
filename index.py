import facebook
import requests
from urllib.parse import urlparse

access_token = "EAAGdXfsupUEBAGYMvXQmQa98BITUlBXiz7ZCyceG6iHAZAfmYPYhXYfZCExDZBBx62WVMOuq8Wf24P4GYgTJTX5BNYCIanSoheO736kPloCKaZAmIrxV2102UbPJwRJ5naxkYLRVP0Umaj91z28h1YFl7C9OAaooZD"
graph = facebook.GraphAPI(access_token=access_token, version="2.1")

# Retrieve information about a website or page:
# https://developers.facebook.com/docs/graph-api/reference/url/
# Note that URLs need to be properly encoded with the "quote" function
# of urllib (Python 2) or urllib.parse (Python 3).
url = urlparse('https://www.facebook.com/groups/149609765847752/?ref=br_rs').geturl()

site_info = graph.get_object(id="149609765847752",
                             fields="og_object")
print(site_info)
