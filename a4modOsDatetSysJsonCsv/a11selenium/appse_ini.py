from selenium import webdriver
from time import sleep

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

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChAuto()
    chrome.acessa('https://github.com/')

    sleep(5)
    chrome.sair()