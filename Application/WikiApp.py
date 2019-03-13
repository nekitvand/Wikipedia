from selenium import webdriver
from Pages.WikiMainPage import WikiMainHepler


class App:

    def __init__(self):
        browser_options = self.browser_options(options='start-maximized')
        self.driver = webdriver.Chrome(chrome_options=browser_options)
        self.wiki = WikiMainHepler(self)
        self.driver.implicitly_wait(10)

    def open_wiki_page(self):
        driver = self.driver
        driver.get("https://ru.wikipedia.org/wiki")

    def destroy(self):
        self.driver.quit()

    def browser_options(self, options):
        chrome_options = webdriver.ChromeOptions()
        if chrome_options.add_argument(options) == 'headless':
            return chrome_options
        else:
            chrome_options.add_argument("start-maximized")
            return chrome_options




