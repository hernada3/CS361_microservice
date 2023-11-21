# CS361_microservice

Requesting data: Once starting the microservice it will be waiting for a request on the url and port it was started on. You can request data by running a post call, and sending a json containing "message_datetime". 
An example call in python would be:
```
#Libraries
import requests
import json

#URL you are going to send the request to
url = 'http://localhost:3000/Time'

#Example JSON that you are sending
message = {
    'message_datetime': '2012-04-23T18:25:43',
    'message_text': 'Yo',
    'message_room_id': 1,
    'message_user_id': 1
}

json_data = json.dumps(message)

#Sending as JSON
headers = {'Content-Type': 'application/json'}

#Example request to the URL, sending the data as JSON
response = requests.post(url, data=json_data, headers=headers)
```



Receiving data: The microservice will return a json with the time held in "Time_Stamp". 

To see what the response is you can add these lines 
```
print(response.status_code)
print(response.json())
```
The response should look something like this:
```
200
{'Time_Stamp': '18:25:43'}
```

# UML Sequence Diagram

![image](https://github.com/hernada3/CS361_microservice/assets/147652557/06d95ea5-a325-4afa-b8bf-b8ca7eae845a)
