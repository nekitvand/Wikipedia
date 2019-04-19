import time
import pytest
from config.config import load_config

load = load_config()


@pytest.mark.parametrize('wiki_words', load.values())
def test_wiki_main_page_parametrize(wikifixture,wiki_words):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.tab_for_discussions()
    wikifixture.wiki.search_words(wiki_words)
    wikifixture.wiki.search_submit()
    time.sleep(1)


@pytest.mark.earth
def test_wiki_main_page(wikifixture):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words(load['Earth'])
    wikifixture.wiki.search_submit()
    time.sleep(1)

@pytest.mark.circle
def test_new_word(wikifixture):
    wikifixture.open_wiki_page()
    assert "Википедия" in wikifixture.driver.title
    assert wikifixture.wiki.assertion_main_page() == True
    wikifixture.wiki.search_words(load['Circle'])
    wikifixture.wiki.search_submit()
    time.sleep(1)


