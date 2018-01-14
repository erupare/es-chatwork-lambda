import requests

# constant
URL = "https://api.chatwork.com/v2"
API_KEY = "your_api_key"
TOKEN_KEY = "X-ChatWorkToken"
headers = {'X-ChatWorkToken': API_KEY}


class ChatWorkClient(object):

    @staticmethod
    def post_messages(message, room_id):

        url = f'{URL}/rooms/{room_id}/messages'
        params = {"body": message}
        response = requests.post(url, headers=headers, params=params)

        return response
