import requests


def sendNotify(msg):
    bot_token = "7760388436:AAH0MVCnhXtOrQ83FrbEMK2CfgRJGP6wfPg"
    chat_id = "@SetecRong_bot"
    html = msg
    html = requests.utils.quote(html)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
    res = requests.get(url)
    return res