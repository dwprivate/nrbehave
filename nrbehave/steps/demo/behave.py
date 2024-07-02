import glob
from textwrap import dedent

from behave import *
from behave.model import Row, Scenario, Table
from behave.parser import parse_file
from behave.runner import Context

# Utils (to move):


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


@given("second operand is {operand:d}")
@given("first operand is {operand:d}")
def step_impl(context, operand):
    operands: list[int] = context.scenario_data.setdefault("operands", [])
    operands.append(operand)


@when("I sum all operands")
def step_impl(context):
    operands: list[int] = context.scenario_data.setdefault("operands", [])
    context.scenario_data["result"] = sum(operands)


@then("result should be {sum:d}")
def step_impl(context: Context, sum):
    assert sum == context.scenario_data["result"]
