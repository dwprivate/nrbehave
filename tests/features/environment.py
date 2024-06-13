from behave import use_fixture
from fixtures import *


def before_all(context):
    print("before_all")


def after_all(context):
    print("after_all")


# == Selenium
def before_tag(context, tag):
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context, timeout=10)
