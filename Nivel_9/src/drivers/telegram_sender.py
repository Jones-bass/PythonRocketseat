import requests

def send_telegram_message(message: str) -> None:
    token = "8698564445:AAGLGCDhfjmcpbJCKkt11kp783qKfaB9-mw"
    chat_id = -1004364527448

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)

#https://api.telegram.org/bot<token>/getUpdates
