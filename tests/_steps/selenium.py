from _utils.selenium_string_utils import *
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('j\'ouvre la page "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@step(
    'je devrais voir un élément "{selector}" contenant le texte "{text}" en moins de {timeout:d} secondes'
)
def step_impl(context, selector, text, timeout):
    wait = WebDriverWait(context.browser, timeout=timeout)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, selector), text))


@when('j\'encode la valeur "{value}" dans le champs "{selector}"')
def step_impl(context, value: str, selector):
    element = context.browser.find_element(By.CSS_SELECTOR, selector)

    element.send_keys(replace_special_keys(value))
