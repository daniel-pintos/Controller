from src.witdirectory import witfile
import speech_recognition as sr
import wit


class Audio(object):
    r = None
    config = witfile.WitMain().config

    def __init__(self):
        self.r = sr.Recognizer()

    def setup(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("< Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    def record_on_terminal(self):
        i = 0
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("Diga alguma coisa... {}".format(i))
            i += 1
            audio = self.r.listen(source)
            fala = self.r.recognize_wit(audio, self.config['Server_Access'], True)
            while fala != 'sair':
                if audio is not None:
                    try:
                        # print(self.r.recognize_google(audio, language="pt", show_all=True))
                        print(self.r.recognize_wit(audio, self.config['Server_Access'], True))
                    except sr.UnknownValueError as error:
                        print("O google não conseguiu entender o que foi falado" + error)
                    except sr.RequestError as e:
                        print("Não foi possivel ter resultados do Google Speech Recogntition; {0}".format(e))
                audio = self.r.listen(source)
                fala = self.r.recognize_wit(audio, self.config['Server_Access'], True)

    def record(self):
        print("fale alguma coisa")
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                intencao = self.r.recognize_wit(audio, self.config['Server_Access'], True)['entities']['Intents'][0]['value']
                return str(intencao)
            except sr.UnknownValueError as error:
                return "error" + error
            except sr.RequestError as e:
                return "error" + e

    def response(self):
        resp = None
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            resp = wit.Wit(self.config['Server_Access']).speech(audio, None, {'Content-Type': 'audio/mpeg3'})
        return resp
