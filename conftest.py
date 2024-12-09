import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_custom_window():
    browser.config.window_height = 800
    browser.config.window_width = 1400
    browser.open('https://google.com/ncr')

    yield
    browser.quit()



