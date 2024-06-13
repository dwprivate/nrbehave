from behave import *


@given('j\'ouvre la page "{url}"')
def step_impl(context, url):
    print(url)


@then(
    'un élément "{selector}" contenant le texte "{text}" apparait en moins de {timeout:d} secondes'
)
def step_impl(context, selector, text, timeout):
    print(timeout)
    print(text)


# @when(u'j\'encode la valeur "python<enter>" dans le champs "input[name="search"]"')
@when('j\'encode la valeur "{value}" dans le champs "{selector}"')
def step_impl(context, value, selector):
    print(value)
