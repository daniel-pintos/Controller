from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class VikiLogin(object):
    login = {
        "cpf": "",
        "senha": ""
    }

    def __init__(self, cpf, password):
        self.google = webdriver.Chrome(
            executable_path="C:\\chromedriver.exe"
        )

    def login_viki(self, cpf, password):
        self.google.get("http://apps.oiviki.com/wplogin.aspx")
        self.login['cpf'] = cpf
        self.login['senha'] = password
        idCpf = "vCPF"
        senha = "vSENHA_SL"
        submitButton = 'ENTRAR'
        google = self.google
        sleep(5)
        cpf_element = google.find_element_by_id(idCpf)
        # bottonSubmit = WebDriverWait(google, 20).until(
        #     lambda google: google.find_element_by_name(submitButton))
        senha_element = google.find_element_by_id(senha)
        bottonSubmit = google.find_element_by_name(submitButton)

        cpf_element.clear()
        cpf_element.send_keys(self.login["cpf"])
        senha_element.clear()
        senha_element.send_keys(self.login["senha"])

        bottonSubmit.click()
        sleep(2)
        bottonSubmit.click()


if __name__ == '__main__':
    login = VikiLogin("08882412911", "#Dani2005")
    login.login_viki()
