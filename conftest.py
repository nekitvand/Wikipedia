import pytest
from Application.WikiApp import App
from Application.api import Api_from_facts


@pytest.fixture(scope="session")
def wikifixture():
    app = App()
    yield app
    app.destroy()



@pytest.fixture(scope="session")
def api():
    facts = Api_from_facts()
    return facts