import time

def test_wiki_main_page(wikifixture):
    wikifixture.open_wiki_page()
    wikifixture.wiki.search_words()
    wikifixture.wiki.search_submit()
    time.sleep(1)