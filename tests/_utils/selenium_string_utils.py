import re

from config import settings
from selenium.webdriver.common.keys import Keys


def replace_special_keys(value):

    for key, val in Keys.__dict__.items():
        if isinstance(val, str) and (val[0:2] != "__"):
            value = value.replace("<" + key + ">", val)
    return value


def replace_env_vars(value):
    if not "{settings:" in value:
        return value
    pattern = r"\{settings:(.*)\}"
    matches = re.findall(pattern, value)
    for key in matches:
        try:
            value = value.replace("{settings:" + key + "}", settings[key])
        except KeyError:
            print(f"ERROR: No value found for key {key} in config files")
            print(
                f'You should add [{key} = "Something"] in settings.toml, or in .secrets.toml if it\'s sensible.'
            )
            print(
                f"In CI/CD you may set environment NRBHAVE_{key} instead of modify config file."
            )
            sys.exit(1)
    return value


def parse_input_text(value):
    value = replace_env_vars(value)
    value = replace_special_keys(value)
    return value
