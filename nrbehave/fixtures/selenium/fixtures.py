from behave import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from nrbehave.utils.selenium_string_utils import *


@fixture
def browser_firefox(context, timeout=2, **kwargs):
    # -- SETUP-FIXTURE PART:
    from selenium.webdriver.firefox.options import Options

    options = Options()
    # options.set_preference("marionette.enabled", False)
    context.browser = webdriver.Firefox(options=options)
    context.browser.implicitly_wait(timeout)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    print("quit browser")
    context.browser.quit()


@fixture
def browser_chrome(context, timeout=2, **kwargs):
    # -- SETUP-FIXTURE PART:
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.accept_insecure_certs = True
    context.browser = webdriver.Chrome(options=options)
    context.browser.implicitly_wait(timeout)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    print("quit browser")
    context.browser.quit()
