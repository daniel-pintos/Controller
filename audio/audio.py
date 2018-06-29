from  witdirectory import witfile
import speech_recognition as sr

class Audio(object):
    r = None

    def __init__(self):
        self.r = sr.Recognizer()

    def audiorecord(self):
        i = 0
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("Diga alguma coisa... {}".format(i))
            audio = self.r.listen(source)
            fala = self.r.recognize_wit(audio, InstanceOfWit.config['Server_Access'], True)
            while fala != 'sair':
                i += 1
                print("Diga alguma coisa... {}".format(i))
                if audio is not None:
                    try:
                        # print(self.r.recognize_google(audio, language="pt", show_all=True))
                        print(self.r.recognize_wit(audio, InstanceOfWit.config['Server_Access'], True))
                    except sr.UnknownValueError as error:
                        print("O google não conseguiu entender o que foi falado" + error)
                    except sr.RequestError as e:
                        print("Não foi possivel ter resultados do Google Speech Recogntition; {0}".format(e))
                audio = self.r.listen(source)
                fala = self.r.recognize_wit(audio, InstanceOfWit.config['Server_Access'], True)

    def record(self):
        i = 0
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            i += 1
            print("Diga alguma coisa... {}".format(i))
            audio = self.r.listen(source)
            return self.r.recognize_google(audio, language="pt", show_all=True)


if __name__ == '__main__':
    wit = InstanceOfWit()
    try:
        Audio().audiorecord()
        # resposta = wit.message(audiotexto)
        # print(resposta)
    except Exception as errorclass:
        print("\n Error:" + errorclass)
