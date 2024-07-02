import time
from contextlib import contextmanager

from behave.runner import Context
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from nrbehave.utils.selenium_string_utils import *


@contextmanager
def virtelIframe(browser: WebDriver, timeout: int = 10) -> WebDriver:
    # skip if already in virtel
    if getattr(browser, "active_frame_id", "") == "virtelEmulator":
        yield browser
    else:
        try:
            wait = WebDriverWait(browser, timeout=timeout)
            wait.until(EC.frame_to_be_available_and_switch_to_it("virtelEmulator"))
            browser.active_frame_id = "virtelEmulator"
            yield browser
        finally:
            browser.switch_to.default_content()
            browser.active_frame_id = ""


def zone_locator(row_y: int, col_x: int):
    """
    Return Selenium locator for span zone with given coordonates
    """
    selector = f"//span[@vr='{row_y}' and @vc='{col_x}']"
    return (By.XPATH, selector)


class VirtelEmulator(object):
    """
    Represents Virtel (MyDesk) emulator, mimics partially py3270 Emulator behavior, with optional Behave Context
    """

    def __init__(self, context, timeout=10):
        self.browser = context.browser
        self.wait = WebDriverWait(self.browser, timeout)

    def setup_myDesk(self):
        with virtelIframe(self.browser):
            time.sleep(0.5)
            self.browser.execute_script("openparmwin()")
            # wait.until(EC.number_of_windows_to_be(2))
            self.browser.switch_to.window(self.browser.window_handles[1])

            self.browser.find_element(By.CSS_SELECTOR, "a#ui-id-3").click()
            self.browser.find_element(
                By.CSS_SELECTOR, 'div#Prm-enter label[for="P-2"]'
            ).click()
            self.browser.find_element(By.CSS_SELECTOR, "button#btn-save").click()
            self.browser.switch_to.window(self.browser.window_handles[0])

    def terminate(self):
        """
        Send logout commands through Virtel
        """
        self.browser.find_element(By.ID, "virtelEmulator").send_keys(
            replace_special_keys("<HOME>FIN<RETURN><PAUSE>/RCL<RETURN>")
        )
        # todo: wit absence of virtelEmulator

    def wait_for_field(self):
        """
        Wait until the screen is ready, the cursor has been positioned
        on a modifiable field, and the keyboard is unlocked.
        """

    def move_to(self, ypos, xpos):
        """
        move the cursor to the given co-ordinates.  Co-ordinates are 1
        based, as listed in the status area of the terminal.
        """
        with virtelIframe(self.browser) as virtel:
            element: WebElement = virtel.find_element(*zone_locator(ypos, xpos))
            assert element.get_attribute("vt") == "I"
            while not (
                virtel.find_element(By.CSS_SELECTOR, "span#sb_cursor").text.strip()
                == f"{ypos},{xpos}"
            ):
                ActionChains(virtel).send_keys(Keys.TAB).perform()

    def send_string(self, tosend: str, ypos=None, xpos=None):
        """
        Send a string to the screen at the current cursor location or at
        screen co-ordinates `ypos`/`xpos` if they are both given.

        Co-ordinates are 1 based, as listed in the status area of the
        terminal.

        Tosend will pe parsed to replace specials keys (contrary to py3270)
        """
        with virtelIframe(self.browser) as virtel:
            if ypos and xpos:
                self.move_to(ypos, xpos)

            ActionChains(virtel).send_keys(replace_special_keys(tosend)).perform()

    def string_get(self, ypos, xpos) -> str:
        """
        Get a string of `length` at screen co-ordinates `ypos`/`xpos`

        Co-ordinates are 1 based, as listed in the status area of the
        terminal.

        Length (as in py3270) in NOT required nor supported
        """
        with virtelIframe(self.browser):
            return self.browser.find_element(*zone_locator(ypos, xpos)).text

    def string_found(self, ypos, xpos, string):
        """
        Return True if `string` is found at screen co-ordinates
        `ypos`/`xpos`, False otherwise.

        Co-ordinates are 1 based, as listed in the status area of the
        terminal.
        """
        with virtelIframe(self.browser) as mydesk:
            return self.wait.until(
                EC.text_to_be_present_in_element(zone_locator(ypos, xpos), string)
            )

    def fill_field(self, ypos, xpos, tosend, length):
        """
        clears the field at the position given and inserts the string
        `tosend`

        tosend: the string to insert
        length: the length of the field

        Co-ordinates are 1 based, as listed in the status area of the
        terminal.

        raises: FieldTruncateError if `tosend` is longer than
            `length`.
        """
        pass

    def get_screen(self):
        """
        Returns the current screen as a list of Ascii strings
        """

        with virtelIframe(self.browser) as virtel:
            text = virtel.find_element(By.CSS_SELECTOR, "pre").text
            # text.replace(" ", "§")
            return text

    def verify_string(self, string, timeout=30):
        """
        Returns True if `string` is found in the screen buffer, False
        otherwise.
        """
        pass

    def find_zones_with_text(self, label: str) -> list[WebElement]:
        """
        Returns list of zones containing given string
        """
        label = label.replace(" ", " ")
        with virtelIframe(self.browser) as virtel:
            return virtel.find_elements(
                By.XPATH, f'//pre//span[contains(text(), "{label}")]'
            )
