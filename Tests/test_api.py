import pytest



def test_cat_facts(api):
    api.facts.cat()