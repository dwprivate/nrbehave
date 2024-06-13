from behave import *


@given("nous avons installé behave")
@given("we have behave installed")
def step_impl(context):
    print("Behave is installed")


@when("nous implémentons un test")
@when("we implement a test")
def step_impl(context):
    print("assert True !")


@then("behave le testera pour nous!")
@then("behave will test it for us!")
def step_impl(context):
    assert True
