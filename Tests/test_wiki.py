import time

def test_wiki_main_page(wikifixture):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words()
    wikifixture.wiki.search_submit()
    assert wikifixture.wiki.assertion_eatrh_page() == "https://ru.wikipedia.org/wiki/%D0%97%D0%B5%D0%BC%D0%BB%D1%8F"
    time.sleep(1)


