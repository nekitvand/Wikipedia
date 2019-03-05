

class WikiMainHepler():

    def __init__(self,app):
        self.app = app
        self.driver = self.app.driver

    def search(self):
        return self.driver.find_element_by_name("search")

    def search_words(self,word):
        self.search().send_keys(word)

    def search_submit(self):
        self.search().submit()

    def assertion_main_page(self):
        return len(self.driver.find_elements_by_css_selector("li[id='pt-login'")) > 0

    def assertion_eatrh_page(self):
        return self.driver.current_url


