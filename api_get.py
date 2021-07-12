import requests # need to install in settings
import json

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(f'Status code = {resp.status_code}')
d = json.loads(resp.content)
print(d)
print(f'id = {d["id"]}')
