

class WikiMainHepler():

    def __init__(self,app):
        self.app = app
        self.driver = self.app.driver

    def search(self):
        return self.driver.find_element_by_name("search")

    def search_words(self):
        self.search().send_keys("Земля")

    def search_submit(self):
        self.search().submit()
