import pytest
from Application.WikiApp import App


@pytest.fixture(scope="session")
def wikifixture():
    app = App()
    yield app
    app.destroy()

