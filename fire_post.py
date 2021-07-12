import requests # need to install in settings
import json

resp = requests.post("http://localhost:8080/coupon", 
              data = '{"id": 4, "title": "shwarma"}',
              headers = {"Content-type": "application/json"});
print(f'Status code = {resp.status_code}');


# how to check if a GET response returned empty??
if resp.content.decode('utf8').replace("'", '"') == '':
   print('empty result')
else:
   print('not empty result')
