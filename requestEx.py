import requests
import json

url = 'http://localhost:3000/Time'

message = {
    'message_datetime': '2012-04-23T18:25:43',
    'message_text': 'Yo',
    'message_room_id': 1,
    'message_user_id': 1
}

json_data = json.dumps(message)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json_data, headers=headers)

print(response.status_code)
print(response.json())
