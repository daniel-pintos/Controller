from src.audio.audio import Audio
from src.witdirectory.witfile import WitMain

if __name__ == '__main__':
    wit = WitMain()
    try:
        Audio().audiorecord()
        # resposta = wit.message(audiotexto)
        # print(resposta)
    except Exception as errorclass:
        print("\n Error:" + errorclass)
