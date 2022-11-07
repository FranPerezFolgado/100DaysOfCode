import requests
import html

BASE_URL = 'https://opentdb.com/api.php'


def get_questions():
    parameters = {
        'amount':20,
        'type':'boolean'
    }
    response = requests.get(url=BASE_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    return html.unescape(data['results'])

