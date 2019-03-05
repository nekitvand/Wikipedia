import time
import pytest
import config


@pytest.mark.parametrize('wiki_words',config.test_data)
def test_wiki_main_page_parametrize(wikifixture,wiki_words):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words(wiki_words)
    wikifixture.wiki.search_submit()
    time.sleep(1)

@pytest.mark.skip
@pytest.mark.earth
def test_wiki_main_page(wikifixture):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words("Земля")
    wikifixture.wiki.search_submit()
    time.sleep(1)

@pytest.mark.skip
@pytest.mark.circle
def test_new_word(wikifixture):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words("Круг")
    wikifixture.wiki.search_submit()
    time.sleep(1)


