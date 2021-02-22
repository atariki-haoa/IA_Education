import requests
import json

r =  requests.get('https://api.covid19tracker.ca/summary')
result = json.loads(r.content)
print(result['data'])
