from selenium import webdriver
from Pages.WikiMainPage import WikiMainHepler
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class App:

    def __init__(self):
        browser_options = self.browser_options(options='start-maximized')
        self.driver = webdriver.Chrome(chrome_options=browser_options)
        self.wiki = WikiMainHepler(self)
        self.driver.implicitly_wait(2)

    def open_wiki_page(self):
        driver = self.driver
        driver.get("https://ru.wikipedia.org/wiki")

    def destroy(self):
        self.driver.quit()

    def element_expected_conditions(self,method,locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((method,locator)))

    def visibility_element_expected_conditions(self,element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(element))

    def browser_options(self, options):
        chrome_options = webdriver.ChromeOptions()
        if chrome_options.add_argument(options) == 'headless':
            return chrome_options
        else:
            chrome_options.add_argument("start-maximized")
            return chrome_options




