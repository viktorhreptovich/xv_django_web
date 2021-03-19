import requests
from .models import TeleSettings


def send_telegram(order_name, order_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message).format(name=order_name, phone=order_phone)

    api = 'https://api.telegram.org/bot'
    method = f'{api}{token}/sendMessage'
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })
