import wit


class WitMain(object):

    config = {
        "Server_Access": "KVK4NH345RMGO4FW7U7U3PBYWPTOY2XS",
        "Client_Access": "4MIYOOWP2X6552JH5CPPYIS6CLT63AEW"
    }

    def __init__(self):
        self.wit = wit.Wit(self.config["Server_Access"])

    def message(self, text='ola mundo'):
        resp = self.wit.message(text)
        return resp['entities']['Intents'][0]['value'] if not None else "deu erro"
