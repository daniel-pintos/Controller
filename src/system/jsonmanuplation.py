import json

"""

:consume string or file
Json:
    import json

dump - escrever em um arquivo
    + json.dump(j, f) 
dumps - escrever em uma string 
    + json.dumps(j)


:return object 
load - carregar de um arquivo
    + json.load(f)
loads - carregar de uma string
    + json.loads(s)

"""


def json_escrever(jsonWrite, path='teste'):
    with open(path + '.json', 'w', encoding='utf-8') as file:
        json.dump(jsonWrite, file)


def json_ler(path='teste'):
    with open(path + '.json', 'r', encoding='utf-8') as file:
        obj1 = json.load(file)
    return obj1
