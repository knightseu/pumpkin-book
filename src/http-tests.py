# http tests
import requests
from pprint import pprint
dest = "https://api.github.com/users/knightseu"
r =requests.get(dest)

pprint(r.headers)

print("------\n\n\n")

pprint(r.text)
