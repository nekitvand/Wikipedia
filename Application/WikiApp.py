from selenium import webdriver
from Pages.WikiMainPage import WikiMainHepler
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.options import Options


class App:

    def __init__(self,browser):
        self.browser = browser
        browser_options = self.browser_options(options='start-maximized')
        if browser == 'yandex':
            self.driver = webdriver.Chrome(executable_path='C:/1/chromedriver.exe', chrome_options=browser_options,)
        elif browser == 'ie':
            ie_options = Options()
            ie_options.ignore_protected_mode_settings = True
            ie_options.ignore_zoom_level = True
            self.driver = webdriver.Ie(executable_path=r'C:\1\IEDriverServer.exe', options=ie_options)
        else:
            raise ValueError
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
        elif chrome_options.add_argument(options) == "start-maximized":
            chrome_options.binary_location = "C:/Users/Vandyshev.NS/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
            return chrome_options



