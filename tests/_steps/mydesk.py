import time
from contextlib import contextmanager

from _utils.selenium_string_utils import *
from behave import *
from behave.runner import Context
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@contextmanager
def emulator(context, timeout=10):
    # skip if already in virtel
    if getattr(context.browser, "active_frame_id", "") == "virtelEmulator":
        yield context.browser
    else:
        try:
            wait = WebDriverWait(context.browser, timeout=timeout)
            wait.until(EC.frame_to_be_available_and_switch_to_it("virtelEmulator"))
            context.browser.active_frame_id = "virtelEmulator"
            yield context.browser
        finally:
            context.browser.switch_to.default_content()
            context.browser.active_frame_id = ""


# to move
def zone_locator(col: int, row: int):  # todo: change signature row, col
    selector = f"//span[@vr='{row}' and @vc='{col}']"
    return (By.XPATH, selector)


@step("textshot")
def textshot(context):
    with emulator(context) as mydesk:
        text = mydesk.find_element(By.CSS_SELECTOR, "pre").text
        text.replace(" ", "§")
        print(text)


@when('I fill in zone {row:d},{col:d} with value "{value}"')
def fill_zone_with_row_and_col(context, row: int, col: int, value: str):
    with emulator(context) as mydesk:
        element: WebElement = mydesk.find_element(*zone_locator(col, row))
        assert element.get_attribute("vt") == "I"
        while not (
            mydesk.find_element(By.CSS_SELECTOR, "span#sb_cursor").text.strip()
            == f"{row},{col}"
        ):
            ActionChains(mydesk).send_keys(Keys.TAB).perform()
        ActionChains(context.browser).send_keys(replace_special_keys(value)).perform()


@when('I fill in zone {where:w} "{label}" with value "{value}"')
def step_impl(context, where: str, label: str, value: str):
    assert where in ["preceding", "following"]
    assert '"' not in label
    # todo
    with emulator(context) as mydesk:
        elements: array[WebElement] = mydesk.find_elements(
            By.XPATH, f'//pre//span[contains(text(), "{label}")]'
        )
        assert len(elements) == 1
        # find the first span with type I after/before given element
        field: WebElement = elements[0].find_element(
            By.XPATH, f'{where}::span[@vt="I"][1]'
        )
        fill_zone_with_row_and_col(
            context, field.get_attribute("vr"), field.get_attribute("vc"), value
        )


@then('zone {row:d},{col:d} should contains value "{value}" within {timeout:d} seconds')
@then('zone {row:d},{col:d} should contains value "{value}"')
# rename: contains text
def zone_with_row_and_col_should_contains(
    context, row: int, col: int, value: str, timeout: int = 10
):
    locator = zone_locator(col, row)
    with emulator(context) as mydesk:
        wait = WebDriverWait(context.browser, timeout=timeout)
        wait.until(EC.text_to_be_present_in_element(locator, value))


@then(
    'zone {where:w} "{label}" should contains value "{value}" within {timeout:d} seconds'
)
@then('zone {where:w} "{label}" should contains value "{value}"')
def step_impl(context, where: str, label: str, value: str, timeout: int = 10):
    assert where in ["preceding", "following"]
    with emulator(context) as mydesk:
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


@when('I send to MyDesk "{value}"')
def step_impl(context, value):
    context.browser.find_element(By.ID, "virtelEmulator").send_keys(
        replace_special_keys(value)
    )


@step("I setup MyDesk")
def setupMyDesk(context):
    driver = context.browser

    with emulator(context):
        time.sleep(1)
        driver.execute_script("openparmwin()")
        # wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        driver.find_element(By.CSS_SELECTOR, "a#ui-id-3").click()
        driver.find_element(By.CSS_SELECTOR, 'div#Prm-enter label[for="P-2"]').click()
        driver.find_element(By.CSS_SELECTOR, "button#btn-save").click()
        driver.switch_to.window(driver.window_handles[0])


@step("I log out")
def logoutMyDesk(context):
    context.browser.find_element(By.ID, "virtelEmulator").send_keys(
        replace_special_keys("<HOME>FIN<RETURN><PAUSE>/RCL<RETURN>")
    )
    print("DISCONNECTED")
    # pass
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
