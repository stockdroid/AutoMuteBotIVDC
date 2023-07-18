import requests
import schedule
import time

bot_token = "INSERT_BOT_TOKEN"
chat_id = *INSERT_CHAT_ID*

def set_restrictions():
    payload = {"chat_id": chat_id, "permissions": {"can_send_messages": False,
                                                "can_send_media_messages": False,
                                                "can_send_polls": False,
                                                "can_send_other_messages": False,
                                                "can_add_web_page_previews": False}}
    response = requests.post(f"https://api.telegram.org/bot{bot_token}/setChatPermissions", json=payload)
    if response.json().get("ok"):
        requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text= 🤐 Il gruppo ha deciso di prendersi una pausa notturna dalle 03:00 alle 06:30, si sente stanco, se vedemo!")
    else:
        set_restrictions()

def remove_restrictions():
    payload = {"chat_id": chat_id, "permissions": {"can_send_messages": True,
                                                "can_send_media_messages": True,
                                                "can_send_polls": True,
                                                "can_send_other_messages": True,
                                                "can_add_web_page_previews": True}}
    response = requests.post(f"https://api.telegram.org/bot{bot_token}/setChatPermissions", json=payload)
    if response.json().get("ok"):
        requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text= 📣 Buongiornooo, la pausa è finita, TACA EL MOTOCAROO!")
    else:
        remove_restrictions()

schedule.every().day.at("03:00").do(set_restrictions)
schedule.every().day.at("06:30").do(remove_restrictions)

while True:
    schedule.run_pending()
    time.sleep(58)
