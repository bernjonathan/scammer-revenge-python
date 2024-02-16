import requests
import time

token = "scammer_bot_token"
message = "your_message"
chat_id = "scammer_chat_id"

url = f"https://api.telegram.org/{token}/sendMessage"

params = {
    "chat_id": chat_id,
    "text": message

}

def send_message():
    try:
        response = requests.get(url, params = params)
        if response.status_code == 200:
            print(response.json())
        else:
            print("Message failed!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
while True:
    send_message()
    time.sleep(0.5)
