# http tests
import requests
import json

from pprint import pprint
dest = "https://api.github.com/users/knightseu"
r =requests.get(dest)

pprint(r.headers)
# parsed = json.dumps(r.headers, indent = 4)
# pprint(parsed)
for a, b in r.headers.items():
    print("{}: {}".format(a, b))
print("------\n\n\n")

pprint(r.text)
