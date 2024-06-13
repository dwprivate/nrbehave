# -- FILE: behave4my_project/fixtures.py  (or in: features/environment.py)
from behave import fixture
from selenium import webdriver


@fixture
def browser_firefox(context, timeout=30, **kwargs):
    # timeout is NOT used !

    # -- SETUP-FIXTURE PART:
    context.browser = webdriver.Firefox()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
