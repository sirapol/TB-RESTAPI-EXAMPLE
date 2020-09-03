import json
import requests
import random
import time

interval = 5

host = "yourHost"
port = 8200
token = "yourToken"
header = {"Content-Tpye": "application/json"}

url = "http://" + host + ":" + str(port) + "/api/v1/" + token + "/telemetry"
print("send to :", url)
try:
    while True:
        strdata = {"data0": str(random.randint(0, 100))}

        jsonData = json.dumps(strdata)
        print(jsonData)
        response = requests.post(url, data=jsonData, headers=header)
        print(response)
        time.sleep(interval)
except KeyboardInterrupt:
    pass