# Controller

Projeto para tratar sobre funções do browser movidas por audio

--------------------

# Flask:

> micro-framework (_framework minimalista_)
>
> * (http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html)

Basea-se em 3 pilares:
    * **WerkZerg** - como deve ser uma interface entre app Python e um web server. Implementação básoca.
    * **Jinha2** - templates: `{{nome varíavel}}` ou `{% for nome in lista_de_nomes %} Hello {{nome}}!! {% endfor %}`.
    * **Good intention**: modo de crescimento de projeto

````shell
# para começar
mkdir wtf
touch wtf/__init__.py
touch wtf/app.py
cd wtf

# criando virtualenvwrapper
sudo apt-get install virtualenvwrapper
mkvirtualenv wtf_env

# ou usando apenas o virtualenv
sudo apt-get install python-virtualenv
virtualenv wtf_env
source wtf_env/bin/activate

#instalando o flask for python
pip install flask
pip install ipython
````

### @code

````py
from flask import flask

# yourapplication/app.py
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! <Strong> I am Learning Flaks</strong>", 200

app.run()
````

O Flask utiliza o import_name para definir o que pertence ao seu projeto e este nome é usado como base path para inferir os recursos como por exemplo descobrir onde fica a sua pasta de templates e sua pasta de arquivos estáticos.

````py
# Supondo que você criará a instancia no caminho yourapplication/app.py você tem essas 2 opções.
    """
    No ultimo caso o __name__ seria yourapplication.app e por isso fazemos o split para se tornar ["yourapplication", "app"] e então pegamos o primeiro elemento.
    """

app = Flask('yourapplication') # passando uma string

# ou a forma com __name__.
app = Flask(__name__.split('.')[0])
````

* O único caso onde uso do `__name__` é recomendado é quando seu projeto se resume a um único arquivo e não está contido em um pacote.

## Sobreescrevendo Flask

Tem duas coisas interessantes nessa forma explicita de criar aplicações no Flask:
    * Uma é o fato de que você pode e é inclusive encorajado a criar suas próprias sub-classes Flask e isso te dá o poder de sobrescrever comportamentos básicos do framework como por exemplo forçar que tudo seja renderizado como JSON (Mas este é um tema que veremos com mais detalhes em outro capítulo).
    * Você pode ter mais de um app Flask em seu projeto e isto te garante reusabilidade e organização, vou dar um exemplo:

````py
# um arquivo projeto.py

web_app = Flask(__name__)

rest_api = Flask(__name__, static_folder="path/to/different/folder")

celery_app = Flask(__name__, instance_path="blablabla")


class FlaskCustomizedForSoap(Flask):
    """Um Flask customizado para sempre responder um objeto SOAP válido"""
    def make_response(self, returned_by_view):
        """faça alguma coisa para nornalizar a
        resposta das views para o padrão SOAP"""
        return soapify(returned_by_view)

soap_api = FlaskCustomizedForSoap(__name__)
````

### View

````py
from flask import Flask, request, render_template

app = Flask("wtf")

@app.route("/noticias/<pais>")
def lista_de_noticias(pais):
    cat = request.args.get("categoria")
    qtd = request.args.get("quantidade")
    noticias = BD.query(pais=pais, categoria=cat).limit(qtd)
    return render_template("lista_de_noticias.html", noticias=noticias), 200

app.run(debug=True, use_reloader=True)
````
Views precisam retornar um objeto do tipo Response ou uma tupla formada por até 3 elementos, um body que pode ser um objeto serializável como por exemplo um texto, um inteiro representando o código de status HTTP e um dicionário de headers, sendo que os dois ultimos elementos são opcionais.

### Regras de URL (_Rules_)

As urls são recebidas no formato texto, por exemplo: /noticias/1, porém em alguns casos queremos que o valor passado como argumento seja convertido para um tipo de dados especifico, ou seja, queremos receber o 1 como um inteiro.

Você já sabe que o Flask utiliza o router do WerkZeug que internamente já implementa alguns conversores para as regras de url.

Os "conversores" padrão são:
    /noticias/<categoria>, recebe o parâmetro "categoria" no formato unicode, exemplo "entretenimento".
    /noticias/<int:noticia_id>, recebe o parâmetro "noticia_id" no formato inteiro, exemplo: "1"
    /cotacao/<float:dolar>/, recebe o parâmetro "dolar" como float, exemplo: "3.2"
    /imagem/<path>, recebe o parâmetro "path" como um caminho, exemplo: "animais/marssupiais/quokka.png"

### A barra no final da url

Isto sempre causa certa confusão, portanto é sempre bom pensar um pouco antes de tomar esta decisão, sua url vai obrigar o uso da trailing backslash ou não?

No Flask existe uma convenção bastante útil: caso você declare sua url sem a barra no final /noticias/<categoria> então esta url será acessível apenas sem a barra no final. Agora se você deseja que a url /noticias/entretenimento/ seja válida declare sua regra como /noticias/<categoria>/ desta forma mesmo que o usuário esqueça de colocar a barra na hora de requisitar a url, o Flask irá automaticamente redirecionar o usuário para a url correta com a "/" no final.

> TIP: Eu costumo utilizar uma lógica simples para decidir sobre o uso da "/", se a url define um recurso final da minha árvore de recursos, por exemplo, se a url é para uma imagem /imagens/foto.jpg ou se é para uma postagem de um site /noticias/apenda-python.html ou até mesmo /noticias/aprenda-python, então eu declaro a url sem a "/" no final. Porém se a url representa uma categoria, uma tag ou uma pasta então coloco a "/" no final pois desta forma segue o conceito de árvore, igual a árvore de arquivos e diretórios. Ex: /noticias/entretenimento/ ou /tags/python/.

## Request

Valores mais importantes do objeto request:

| tipo | Discrição |
| ---- | --------- |
| `request`.method: | Informa qual método HTTP foi usado na requisiçao |
| `request`.headers: | headers HTTP da requisição, útil para checar o mimetype e dados de basic auth. |
| `request`.environ: | Variáveis de ambiente do WSGI, navegador, ip do cliente etc |
| `request`.path | `request`.url: O path ou a url completa da requisição |
| `request`.is_xhr: | Informa se é ou não uma requisição Ajax |
| `request`.blueprint: |Nome do blueprint que interceptou o request, Blue o que? -- Calma, veremos o que é isso mais adiante |

##### request.args

* request.args = retonra uma classe `ImmutableMultiDict([('categoria', u'esportes'), ('limit', u'10')])`
* request.args.to_dict() = transforma para um dicionário
* request.args.get("categoria") = pega apenas um valor


------------------

# Selenium

### requiredments

* `geckodriver` - driver para o Firefox
* bibliotecas do python:
  - selenium
  ```shell
  sudo pip install selenium
  ```

### @code

automatização de scripts:

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
browser.get('http://www.google.com.br')
assert "Google" in browser.title
elem = browser.find_element_by_id("lst-ib")
elem.clear()
elem.send_keys("Rafinha o melhor do mundo")
elem.send_keys(Keys.RETURN)
assert "No results found" not in browser.page_source
```
