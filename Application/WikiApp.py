from selenium import webdriver
from Pages.WikiMainPage import WikiMainHepler


class App:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wiki = WikiMainHepler()

    def open_wiki_page(self):
        driver = self.driver
        driver.get("https://ru.wikipedia.org/wiki")

    def destroy(self):
        self.driver.quit()

