import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_config():
    browser.config.window_width = "1920"
    browser.config.window_height = "1080"

    browser.open("https://scan-interfax.ru/")
    yield
    browser.close()
