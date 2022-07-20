import requests

BOT_URL = 'https://api.telegram.org/bot{}'  # <-- add your telegram token as environment variable

class TelegramApi():
  def __init__(self, token):
    self._token = token
  
  def send_message(self, chat_id, message, reply_markup=None):
        url = BOT_URL.format(self._token) + '/sendMessage'
        data = {'chat_id': chat_id, 'text': message, 'parse_mode': 'HTML'}
        if reply_markup:
          data['reply_markup'] = reply_markup
        r = requests.post(url, data=data)
        if r.status_code == 200:
          return r.json()
        return None

  def get_me(self):
      url = f"https://api.telegram.org/bot{self._token}/getMe"
      response = requests.get(url)
      if response.status_code == 200:
          salida = json.loads(response.text)
          return salida
      return None

  def get_updates(self):
      url = f"https://api.telegram.org/bot{self._token}/getUpdates"
      print(url)
      response = requests.get(url)
      if response.status_code == 200:
          salida = json.loads(response.text)
          return salida
      return None
