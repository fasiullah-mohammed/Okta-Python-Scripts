import requests
import json


api_token='enter your token'
url = "https://yourdomain.okta.com/api/v1/users/"

payload = ""
headers = {
'Accept': "application/json",
'Content-Type': "application/json",
'Authorization': "SSWS "+ "Enter your token"

}

response = requests.request("GET", url, data=payload, headers=headers).json()
print(response)
with open('Active users.json', 'w') as file:
    json.dump(response, file)
