import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)


token = "8698564445:AAGLGCDhfjmcpbJCKkt11kp783qKfaB9-mw"
chat_id = -1004364527448
message = "Estou no telegram em Python!"

send_telegram_message(token, chat_id, message)
