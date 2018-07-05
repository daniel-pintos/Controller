from src.system.controller import VikiLogin
from src.system.jsonmanuplation import json_ler
from src.audio.audio import Audio

import src.system

from sys import stdin
import getpass


def senha_criptografada():
    return getpass.getpass('Senha: ') if stdin.isatty() else input("Senha: ")


if __name__ == '__main__':
    json = json_ler()
    json_audio = Audio()
    login = VikiLogin()
    login.login_viki(json['cpf'], json['senha'])
    json_audio.setup()
    # if json_audio.record().lower() == "abrir um processo":
    #     login.novo_process()
