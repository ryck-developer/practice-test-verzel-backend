import requests
import json

# TESTE_01 - testando recebimento do token refresh
url = "http://localhost:8000/api/token/"
data = {"username": "admin", "password": "admin"}
headers = {'Content-type': 'application/json'}

r = requests.post(
    url, 
    data=json.dumps(data), 
    headers=headers
)
print(r.text)
#FIM TESTE_01
