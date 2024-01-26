import requests
import json
import time


token = "6984990599:AAEtH2IiB3tyymOyV_BzrSOjLao6uYOnp0o"
chat_ids = [270756677, 362800141]


for chat_id in chat_ids:
    data = json.dumps({
        "chat_id": chat_id,
        "text": "POLINKAAAAAA"
    })
    headers = {
        "Content-Type": "application/json"
    }

    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data, headers=headers)

    # time.sleep(1)

# response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
# print(response.json())