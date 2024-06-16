from _fixtures.fixtures import *
from behave import use_fixture


def before_tag(context, tag):
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context, timeout=10)
    elif tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context, timeout=10)
