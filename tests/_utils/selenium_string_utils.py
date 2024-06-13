from selenium.webdriver.common.keys import Keys


def replace_special_keys(value):

    for key, val in Keys.__dict__.items():
        if isinstance(val, str) and (val[0:2] != "__"):
            value = value.replace("<" + key + ">", val)
    return value
