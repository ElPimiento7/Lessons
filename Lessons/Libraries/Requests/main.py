import requests

headers = {
    'User-Agent': "Abracadabra"
}

page = "https://httpbin.org/get"
response = requests.get(page, headers=headers, params={"a": "b", "c": 10})

if response.status_code == 200:
    print("OK")
if response.ok:
    print("OK")

response.raise_for_status()

print(response.text)
print(response.json())
print("---------------------")

page2 = "https://httpbin.org/post"
response1 = requests.post(page2,
                          headers=headers,
                          params={"a": "b", "c": 10},
                          json={"username": "kuritsa"})

print(response1.text)
