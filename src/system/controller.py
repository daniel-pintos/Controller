from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class VikiLogin(object):
    href = {
        "processo": "http://10.1.2.13/viki/wpPainelProcessos.aspx",
        "cards": "http://10.1.2.13/viki/wpMeusCards.aspx",
        "busca de vagas": "http://10.1.2.13/viki/wpLocalizaVagas.aspx",
        "jogos": "http://10.1.2.13/viki/wppaineljogos.aspx",
        "carona": "http://10.1.2.13/viki/wpmapacaronas.aspx",
        "megafone": "http://10.1.2.13/viki/wwtsmegafone.aspx",
        "feedback": "http://10.1.2.13/viki/wwtsfeedback.aspx",
        "banca digital": "http://10.1.2.13/viki/wpBancaDigital.aspx",
        "holerite": "http://10.1.2.13/viki/wpHolerite.aspx",
        "transações": "http://10.1.2.13/viki/wpCarteiraUsuario.aspx",
        "comprar moedas": "http://10.1.2.13/viki/wpCompramoedasusuario.aspx",
        "transferir moedas": "http://10.1.2.13/viki/wpTransfCarteiraUsuario.aspx",
        "efetuar saque": "http://10.1.2.13/viki/wpSaqueUsuario.aspx",
        "sobre": "http://10.1.2.13/viki/wpSobre.aspx",
        "avaliação operacional": "http://10.1.2.13/viki/wpAvaliacaoProfissional.aspx",
        "avaliação feedback": "http://10.1.2.13/viki/wwtsAvaliacaoFeedback.aspx",
        "equipes": "http://10.1.2.13/viki/wpequipe.aspx"
    }

    def __init__(self, path="C:\\chromedriver.exe"):
        self.google = webdriver.Chrome(
            executable_path=path
        )

    def login_viki(self, cpf, password):
        self.google.get("http://10.1.2.13/viki/wplogin.aspx")
        google = self.google
        sleep(3)
        cpf_element = google.find_element_by_id("vCPF")
        senha_element = google.find_element_by_id("vSENHA_SL")
        botton_submit = google.find_element_by_name('ENTRAR')
        try:
            cpf_element.clear()
            senha_element.clear()
            cpf_element.send_keys(cpf)
            senha_element.send_keys(password)

            botton_submit.click()
            try:
                # ouvir o que o usuário vai querer
                sleep(2)
                botton_submit.click()
            except TimeoutError as timeOut:
                print(timeOut)
        except Exception as error:
            print(error)

    def novo_process(self):
        sleep(3)
        workflow = self.google.find_element_by_class_name("sidebar")
        ul = workflow.find_element_by_class_name("sidebar-menu")
        list = [lista for lista in ul.find_elements_by_tag_name("li")]
        element = list[2]
        element.click()
        element.find_element_by_class_name("processos").click()

    def processo(self):
        pass

    def menu_div(self):
        sleep(3)
        # div = self.google.find_element_by_id('gxHTMLWrpW0046')
        div = self.google.find_element_by_class_name('daniellindao')
        print(div)

    # TODO: fazer com que ele consiga achar a referencia.
    # ao invés de insirar o link direto para a pessoa fazer busca
    def process_not_used(self):
        sleep(3)
        div = self.google.find_element_by_class_name("daniellindao")
        try:
            list = [elemenet for elemenet in div.find_elements_by_tag_name('a')]
            # classe = div.find_element_by_class_name('buscadevagas')
            # classe.click()
        except Exception as error:
            print(error)
