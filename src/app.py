#!/usr/bin/env python3
from flask import Flask, request, jsonify, make_response
from telegramApi import TelegramApi
import os, sys , re, json, time, requests

#BOT_URL = f'https://api.telegram.org/bot{os.environ["{BOT_KEY}"]}/'  # <-- add your telegram token as environment variable

app = Flask(__name__)

page = 'https://api.coingecko.com/api/v3/coins/'
PATTERN = r'(.*polla.*|culo|inutil|.*puta.*|hdp|gili)'

telegramApi = TelegramApi(os.environ["BOT_KEY"])

def logger(message):
    timestamp = time.strftime('%y-%m-%d %H:%M:%S', time.gmtime())
    sys.stdout.write('{} | {}\n'.format(timestamp, message))


def answer(word):
    api = requests.get(f'{page}{word}')
    json_data = json.loads(api.content)
#    logger(json.dumps(json_data, indent=4, sort_keys=True))
    if "market_data" in json_data:
        market_data = json_data["market_data"]["current_price"]["eur"]
        market_cap = json_data["market_data"]["market_cap"]["eur"]
        links = json_data["links"]["homepage"][0]
        symbol= json_data["symbol"]
        msg = f"Symbol: {symbol}\nPrecio actual: {market_data}€\nCapital de Mercado: {market_cap}€\nPagina oficial: {links}"
        return msg

@app.route('/status', methods=['GET'])
def get_status():
    return 'Up and running', 201


@app.route('/webhook', methods=['GET', 'POST'])
def main():
    try:
        if request.method == 'GET' or not request.json:
            return 'OK', 200
    except Exception:
        return 'OK', 200
    payload = request.json
    logger(json.dumps(payload, indent=4, sort_keys=True))
    if "message" in payload:
        chat_id = payload["message"]["chat"]["id"]
        msg = payload["message"]["text"]
        message = answer(msg.lower())
        telegramApi.send_message(chat_id, message)
        if re.match(PATTERN, payload["message"]["text"], re.IGNORECASE):
            message = "Eso no se dice"
            telegramApi.send_message(chat_id, message)
            logger(json.dumps(payload, indent=4, sort_keys=True))
        elif payload["message"]["text"] == "/enlaces":
            message = "Enlaces de interes"
            buttons = []
            buttons.append({"text": "Informacion",
                           "url": "https://telegra.ph/The-Best-c0in-01-19"})
            buttons.append({"text": "Google",
                           "url": "https://google.es"})
            inline_keyboard = json.dumps({"inline_keyboard": [buttons]})
            telegramApi.send_message(chat_id, message, inline_keyboard)
    elif "channel_post" in payload:
        chat_id = payload["channel_post"]["chat"]["id"]
        msg = payload["channel_post"]["text"]
        message = answer(msg.lower())
        telegramApi.send_message(chat_id, message)
        if re.match(PATTERN, payload["channel_post"]["text"], re.IGNORECASE):
            message = "Eso no se dice"
            telegramApi.send_message(chat_id, message)
            logger(json.dumps(payload, indent=4, sort_keys=True))
        elif payload["channel_post"]["text"] == "/enlaces":
            message = "Enlaces de interes"
            buttons = []
            buttons.append({"text": "Informacion",
                           "url": "https://telegra.ph/The-Best-c0in-01-19"})
            buttons.append({"text": "Google",
                           "url": "https://google.es"})
            inline_keyboard = json.dumps({"inline_keyboard": [buttons]})
            telegramApi.send_message(chat_id, message, inline_keyboard)
    return 'OK', 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)


if __name__ == '__main__': 
    logger("\n\n[!] Arrancando maquinas....\n\n")
    logger("\t\n[*] Bot iniciado\n\n")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
