import requests


def sendNotify(msg):
    bot_token = "6905649849:AAFne7QLbZEfFtOiDtEDsCPp2N6lAQFZSZI"
    chat_id = "@cheng123677"
    html = msg
    html = requests.utils.quote(html)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
    res = requests.get(url)
    return res