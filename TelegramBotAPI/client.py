
import requests
from TelegramBotAPI.types.type import Type


class Client(object):

    def __init__(self, token, proxy=None):
        self.__token = token
        self.__proxies = None
        if proxy:
            self.__proxies = {"https": "https://%s" % proxy}

    def __method_url(self, method):
        return 'https://api.telegram.org/bot%s/%s' % (self.__token, method)

    def post(self, method):
        url = self.__method_url(method._name)
        raw = method._to_raw()
        rsp = requests.post(url, data=raw, proxies=self.__proxies)
        value = rsp.json()
        if value['ok'] == True:
            return Type._new(value['result'], type=type)
        print value
