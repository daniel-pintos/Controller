from src.system.controller import VikiLogin
from src.system.jsonmanuplation import json_ler
from src.audio.audio import Audio

import src.system

from sys import stdin
import getpass


def comparation_array_small(elem, array1):
    for array_elements in array1:
        if elem in array_elements:
            return True
    return False

def senha_criptografada():
    return getpass.getpass('Senha: ') if stdin.isatty() else input("Senha: ")


if __name__ == '__main__':
    json = json_ler()
    audio = Audio()
    # TODO: alterar para fazer com a páginação
    login = VikiLogin()
    login.login_viki(json['cpf'], json['senha'])
    audio.setup()
    dict_json = VikiLogin.href
    hret = [key.title().lower() for key in VikiLogin.href]

    print("--"*10 + " começando " + "--"*10)
    for link in dict_json.values():
        print(str(dict_json.get(link)) + " | " + link)
    res = audio.record()
    lista = [entities for entities in res['entities']]
    sublista = [res['entities'][subelement][0]['value'] for subelement in lista]
    for values in sublista:
        if comparation_array_small(values, hret):
            if values == 'processo':
                print('abrir processo')
                login.novo_process()
        else:
            print('não foi encontrado')

