import http.client
import json

conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

payload = {
    "messages": [
        {
            "role": "user",
            "content": "Сформувати документ на основній темі Component Design Document (CDD)"
        }
    ],
    "temperature": 0.9,
    "top_k": 5,
    "top_p": 0.9,
    "max_tokens": 256,
    "web_access": False
}

payload_encoded = json.dumps(payload).encode('utf-8')

headers = {
    'x-rapidapi-key': "6b060f05c7msh53183ba8b89206dp1a7d22jsn6a688890bc9f",
    'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/geminipro", body=payload_encoded, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
