import pytest
from Application.WikiApp import App
from Application.api import Api_from_facts



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="yandex")


@pytest.fixture(scope="session")
def wikifixture(request):
    browser = request.config.getoption("--browser")
    app = App(browser)
    yield app
    app.destroy()



@pytest.fixture(scope="session")
def api():
    facts = Api_from_facts()
    return facts