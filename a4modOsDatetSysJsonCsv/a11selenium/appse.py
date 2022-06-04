from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


class ChAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=Perfil')
        self.options.add_argument('user-data-dir=c:\\Path')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def click_signin(self):
        try:
            # btn_signin = self.chrome.find_element_by_link_text('Sign in')
            btn_signin = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_signin.click()
        except Exception as e:
            print('Erro ao clicar Sign in: ', e)

    def acessa(self, site):
        self.chrome.get(site)

    def loga(self):
        try:
            in_login = self.chrome.find_element(By.ID, 'login_field')
            in_pass = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')
            in_login.send_keys('leoemcasa')
            in_pass.send_keys('')
            sleep(5)
            btn_login.click()
            sleep(3)
        except Exception as e:
            print('Erro ao logar: ', e)

    def clica_perf(self):
        try:
            perf = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex')
            perf.click()
            sleep(3)
        except Exception as e:
            print('Erro ao clicar perf: ', e)

    def logout(self):
        try:
            perf = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perf.click()
        except Exception as e:
            print('Erro ao logout: ', e)

    def check_usr(self, usr):
        prof_link = self.chrome.find_element(By.CLASS_NAME, 'user-profile-link')
        prof_link_html = prof_link.get_attribute('innerHTML')
        assert usr in prof_link_html


    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    print(os.environ['COMPUTERNAME'])
    chrome = ChAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perf()
    chrome.logout()

    chrome.click_signin()
    chrome.loga()
    chrome.clica_perf()
    chrome.check_usr('leoemcasa')


    sleep(5)
    chrome.sair()
