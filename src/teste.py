from src.system.controller import VikiLogin
from src.witdirectory.witfile import WitMain


def comparation_array_small(elem, array1):
    for array_elements in array1:
        if elem in array_elements:
            return True
    return False


if __name__ == '__main__':
    hret = [key.title().lower() for key in VikiLogin.href]
    print(hret)
    resp = WitMain().message_response('viki, abra um processo e transferira dinheiro')
    lista = [entities for entities in resp['entities']]
    sublista = [resp['entities'][subelement][0]['value'] for subelement in lista]
    for values in sublista:
        if comparation_array_small(values, hret):
            if values == 'processo':
                print('abrir processo')
        else:
            print('não foi encontrado')
