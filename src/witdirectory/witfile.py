import wit


class WitMain(object):
    config = {
        "Server_Access": "KVK4NH345RMGO4FW7U7U3PBYWPTOY2XS",
        "Client_Access": "4MIYOOWP2X6552JH5CPPYIS6CLT63AEW"
    }

    def __init__(self):
        self.wit = wit.Wit(self.config["Server_Access"])

    @classmethod
    def message(cls, text='ola mundo'):
        resp = cls.wit.message(text)
        return resp['entities']['Intents'][0]['value'] if not None else "deu erro"

    def message_response(self, texto='olá viki'):
        return self.wit.message(texto)
