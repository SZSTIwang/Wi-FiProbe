import requests
import json
headers = {'content-type':'application/json'}
url="http://192.168.1.20:8888/register/"   #IP和端口号，注意register后要加/
data = {
    'taskId':"11",
    'shareDir':'sharedir',
    'url':'url',
    'name':'Name'
}
r = requests.post(url, data=json.dumps(data),headers=headers)
print(r.text)