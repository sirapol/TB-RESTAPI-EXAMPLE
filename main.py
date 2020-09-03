import json
import requests
import random

host = "58.64.25.160"
port = 8200
token = "pAge7KRCDZu6ET85NHb8"
header = {"Content-Tpye":"application/json"}

strdata = {"data0":str(random.randint(0,100))}

url = "http://" + host + ":" + str(port) + "/api/v1/" + token + "/telemetry"

print("send to :",url)
jsonData = json.dumps(strdata)
print(jsonData)
response = requests.post(url,data=jsonData,headers=header)
print(response)