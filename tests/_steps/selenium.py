from _utils.selenium_string_utils import *
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('I visit "{url}"')
@step('j\'ouvre la page "{url}"')
def step_impl(context, url):
    context.browser.get(url)
    context.attach("text/plain", "screenshot_image".encode())


@step(
    'je devrais voir un élément "{selector}" contenant le texte "{text}" en moins de {timeout:d} secondes'
)
def step_impl(context, selector, text, timeout):
    wait = WebDriverWait(context.browser, timeout=timeout)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, selector), text))


@when('I fill in element "{selector}" with value "{value}"')
@when('j\'encode la valeur "{value}" dans le champs "{selector}"')
def step_impl(context, value: str, selector):
    element = context.browser.find_element(By.CSS_SELECTOR, selector)

    element.send_keys(parse_input_text(value))


@when('I press element "{selector}"')
def step_impl(context, selector):
    element = context.browser.find_element(By.CSS_SELECTOR, selector)

    element.click()


@then('the browser\'s URL should match "{partial_url}" within {timeout:d} seconds')
def step_impl(context, partial_url, timeout):
    wait = WebDriverWait(context.browser, timeout=timeout)
    wait.until(EC.url_matches(partial_url))
