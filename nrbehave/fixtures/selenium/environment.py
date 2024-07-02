from behave import use_fixture

from nrbehave.fixtures.selenium.fixtures import *


def before_tag(context, tag):
    print("before tag " + tag)
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context, timeout=10)
    elif tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context, timeout=10)


def after_tag(context, tag):
    print("after tag " + tag)
    if tag == "autoLogout":
        context.execute_steps("Then I log out")
