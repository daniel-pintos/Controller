from flask import Flask, jsonify, current_app, session, redirect, url_for, escape, request, render_template
from src.audio.audio import Audio
from src.system.controller import VikiLogin

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"


def comparation_array_small(elem, array1):
    for array_elements in array1:
        if elem in array_elements:
            return True
    return False


@app.route('/')
def index():
    return render_template("index.html"), 200


# O escape() precisa ser usado apenas se você não estiver usando um template.
@app.route('/audio', methods=['GET', 'POST'])
def record():
    audio = Audio()
    audio.setup()
    dict_json = VikiLogin.href
    hret = [key.title().lower() for key in VikiLogin.href]
    print("--" * 10 + " começando " + "--" * 10)
    for link in dict_json.values():
        print(str(dict_json.get(link)) + " | " + link)
    res = audio.record()
    lista = [entities for entities in res['entities']]
    sublista = [res['entities'][subelement][0]['value'] for subelement in lista]
    for values in sublista:
        if comparation_array_small(values, hret):
            return values
        else:
            print('não foi encontrado')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
