from selenium.webdriver.common.by import By


class WikiMainHepler:

    def __init__(self,app):
        self.app = app
        self.driver = self.app.driver

    def search(self):
        return self.app.element_expected_conditions(By.NAME, "search")

    def search_words(self,word):
        self.search().send_keys(word)

    def search_submit(self):
        self.search().submit()

    def assertion_main_page(self):
        return len(self.driver.find_elements_by_css_selector("li[id='pt-login']")) > 0

    def assertion_earth_page(self):
        return self.driver.current_url

    def tab_for_discussions(self):
        element = self.driver.find_element_by_id("ca-talk")
        if self.app.visibility_element_expected_conditions(element):
            return True
        else:
            return False and self.app.destroy()


