import os
import json
import pytest
from config.config import load_animal_facts

load = load_animal_facts()

def test_cat_facts(api):
    cat_facts = api.facts.cat()
    assert cat_facts[0]["type"] == "cat" and cat_facts [1]["type"] == "cat"
    assert cat_facts[0]["text"] != '' or None and cat_facts [1]["text"] != '' or None

def test_dog_facts(api):
    dog_facts = api.facts.dog()
    assert dog_facts[0]["type"] == "dog" and dog_facts [1]["type"] == "dog"
    assert dog_facts[0]["text"] != '' or None and dog_facts [1]["text"] != '' or None


def test_yandex_translate(api):
    translate = api.facts.yandex_translate()
    assert translate["text"] != '' or None
    with open((os.path.abspath(r"..\animal_facts.json")),'w+',encoding="UTF-8") as f:
        f.write(json.dumps(translate["text"],ensure_ascii=False))

@pytest.mark.parametrize("animal_facts",load)
def test_yandex_translate_multilang(api,animal_facts):
    translate = api.facts.yandex_translate_multilang(lang='ru-en',text=animal_facts)
    assert translate["text"] != '' or None
    print(translate)
