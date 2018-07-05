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
    audio = Audio()
    # TODO: alterar para fazer com a páginação
    # login = VikiLogin()
    # login.login_viki(json['cpf'], json['senha'])
    audio.setup()
    dict_json = VikiLogin.href
    print("--"*10 + " começando " + "--"*10)
    for link in dict_json.values():
        print(str(dict_json.get(link)) + " | " + link)

