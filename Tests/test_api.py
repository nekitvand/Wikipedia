

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

