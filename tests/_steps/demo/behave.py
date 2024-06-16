import glob
from textwrap import dedent

from behave import *
from behave.model import Row, Scenario, Table
from behave.parser import parse_file
from behave.runner import Context


# Utils (to move):
def parse_scenrario_with_row(text: str, row: Row):
    for heading in row.headings:
        text = text.replace(f"<{heading}>", row[heading])
    return text


def scenario_to_txt(scenario: Scenario):
    # all_steps include background steps
    return "\n".join([f"{step.keyword} {step.name}" for step in scenario.all_steps])


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


@given("a scenario")
def step_impl(context: Context):
    text: str = context.text
    context.scenario_data["scenario"] = dedent(text)


@when("I execute it")
def step_impl(context: Context):
    try:
        context.scenario_data["success"] = context.execute_steps(
            context.scenario_data["scenario"]
        )

    except AssertionError as e:
        context.scenario_data["success"] = False
        context.scenario_data["error"] = e


@when("I execute it with data")
def step_impl(context: Context):
    datatable: Table = context.table
    iterator = iter(datatable)
    context.scenario_data["success"] = (
        True  # up to now, scenario is successful. It could be better to use enum status
    )
    try:
        while context.scenario_data["success"]:
            row = next(iterator)
            scenario_with_data: str = parse_scenrario_with_row(
                context.scenario_data["scenario"], row
            )
            try:
                context.scenario_data["success"] = context.execute_steps(
                    scenario_with_data
                )

            except AssertionError as e:
                context.scenario_data["success"] = False
                context.scenario_data["error"] = e
    except StopIteration:
        pass


@then("it should return success")
def step_impl(context):
    assert context.scenario_data["success"]


@then("it should return failed")
def step_impl(context):
    assert not (context.scenario_data["success"])


@given('a glob "{glob}"')
def step_impl(context, glob: str):
    context.glob = glob


@when("I search for files using this glob")
def step_impl(context):
    # à partir du répertoire courant...
    context.files = glob.glob(context.glob, recursive=True)


@then("I should find {nb:d} file")
def step_impl(context, nb):
    assert len(context.files) == nb


@when('I search for scenario "{title}" in this file')
def step_impl(context, title):
    feature = parse_file(context.files[0])
    context.matching_scenarios = [
        scenario for scenario in feature.scenarios if scenario.name == title
    ]


@then("I should find 1 scenario")
def step_impl(context):
    assert len(context.matching_scenarios) == 1


@when("I execute this scenario")
def step_impl(context):
    scenario_as_text = scenario_to_txt(context.matching_scenarios[0])
    try:
        context.scenario_data["success"] = context.execute_steps(scenario_as_text)

    except AssertionError as e:
        context.scenario_data["success"] = False
        context.scenario_data["error"] = e
