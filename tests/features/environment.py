from _hooks.selenium import *
from behave import use_fixture


def before_all(context):
    print("before_all")


def after_all(context):
    print("after_all")
