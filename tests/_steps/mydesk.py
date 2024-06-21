import time

from _utils.virtel import VirtelEmulator, virtelIframe
from behave import *
from behave.runner import Context
from selenium.webdriver.common.by import By


@step("textshot")
def textshot(context):
    print(VirtelEmulator(context).get_screen())


@when('I fill in zone {row:d},{col:d} with value "{value}"')
def fill_zone_with_row_and_col(context, row: int, col: int, value: str):
    VirtelEmulator(context).send_string(value, row, col)


@when('I fill in zone {where:w} "{label}" with value "{value}"')
def step_impl(context, where: str, label: str, value: str):

    match where:
        case "following" | "after":
            xpath_suffix: str = f'following::span[@vt="I"][1]'
        case "preceding" | "before":
            xpath_suffix: str = f'preceding::span[@vt="I"][1]'
        case _:
            raise ValueError('Unexpected "where" keyword: ' + where)

    assert '"' not in label  # todo
    elements: array[WebElement] = VirtelEmulator(context).find_zones_with_text(label)
    assert len(elements) == 1
    with virtelIframe(context.browser):
        field: WebElement = elements[0].find_element(By.XPATH, xpath_suffix)
        ypos = field.get_attribute("vr")
        xpos = field.get_attribute("vc")
    VirtelEmulator(context).send_string(value, ypos, xpos)


@then('zone {row:d},{col:d} should contains value "{value}" within {timeout:d} seconds')
@then('zone {row:d},{col:d} should contains value "{value}"')
# rename: contains text
def zone_with_row_and_col_should_contains(
    context, row: int, col: int, value: str, timeout: int = 10
):

    assert VirtelEmulator(context, timeout).string_found(row, col, value)


@then(
    'zone {where:w} "{label}" should contains value "{value}" within {timeout:d} seconds'
)
@then('zone {where:w} "{label}" should contains value "{value}"')
def step_impl(context, where: str, label: str, value: str, timeout: int = 10):
    assert where in ["preceding", "following"]
    with virtelIframe(context) as mydesk:
        elements: array[WebElement] = mydesk.find_elements(
            By.XPATH, f'//pre//span[contains(text(), "{label}")]'
        )
        assert len(elements) == 1
        # find the first span with type I before given element
        field: WebElement = elements[0].find_element(
            By.XPATH, where + '::span[@vt="I"][1]'
        )
        zone_with_row_and_col_should_contains(
            context,
            field.get_attribute("vr"),
            field.get_attribute("vc"),
            value,
            timeout,
        )


@when('I press keys "{value}" in myDesk')
def step_impl(context, value):
    VirtelEmulator(context).send_string(value)


@step("I setup MyDesk")
def setupMyDesk(context):
    VirtelEmulator(context).setup_myDesk()


@step("I log out")
def logoutMyDesk(context):
    VirtelEmulator(context).terminate()
    # context.browser.switch_to.default_content()
    # try:
    #     # WebDriverWait(context.browser, timeout=2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "app-nav-more")))
    #     WebDriverWait(context.browser, timeout=30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    #     context.browser.find_element(By.CSS_SELECTOR, "app-nav-more").click()
    #     context.browser.find_elements(By.CSS_SELECTOR, "app-nav-more div.nav__more-menu__item")[1].click()
    #     WebDriverWait(context.browser, timeout=2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "app-connexion")))
    #     print("disconnected")
    # except Exception as e:
    #     print(f"NOT disconnected: {e}")


@step('I go to screen "{screen}"')
def goToMyDeskScreen(context: Context, screen: str):
    context.browser.get(
        f"https://mydesk-tst.ethias.be/terminal?actionKey={screen}&actionType=100"
    )
    time.sleep(1)  # to improve, maybe with loader
