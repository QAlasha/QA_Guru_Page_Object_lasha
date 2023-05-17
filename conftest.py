import time
from selene import browser
import pytest


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = ("https://demoqa.com")
    browser.config.window_width = 1080
    browser.config.window_height = 1000
    time.sleep(3)
    yield
    browser.quit()