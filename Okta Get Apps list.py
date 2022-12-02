from http.client import responses
import requests
import json


api_token='Enter your token'
url = "https://yourdomain.okta.com/api/v1/apps/"

payload = ""
headers = {
'Accept': "application/json",
'Content-Type': "application/json",
'Authorization': "SSWS "+ "Enter your token"

}

data = requests.request("GET", url, data=payload, headers=headers).json()
print(data)
with open('Apps_list.json', 'w') as file:
    json.dump(data, file)

   
    
