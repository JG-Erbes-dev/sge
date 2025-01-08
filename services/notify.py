import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/3b1744c5-b432-4183-8e91-2b619d071a49',
            json=data,
        )
