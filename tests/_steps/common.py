import glob

from behave import *
from behave.model import Feature, Row, Scenario, Table
from behave.parser import parse_file
from behave.runner import Context

# Behave utilities


def scenario_to_txt(scenario: Scenario, row: Row = None):
    # all_steps include background steps
    text: str = "\n".join(
        [f"{step.keyword} {step.name}" for step in scenario.all_steps]
    )
    if row:
        for heading in row.headings:
            text = text.replace(f"<{heading}>", row[heading])
    return text


def load_scenario_from_feature_file(feature_glob: str, scenario_title: str) -> Scenario:
    files = glob.glob(f"**/{feature_glob}.feature", recursive=True)
    assert len(files) == 1
    feature_object: Feature = parse_file(files[0])
    matching_scenarios = [
        scenario
        for scenario in feature_object.scenarios
        if scenario.name == scenario_title
    ]
    assert len(matching_scenarios) == 1
    return matching_scenarios[0]


@step("breakpoint")
def breakpoint(context):
    pass


@step("it should succeed")
def succeed(context):
    pass


@step('I run scenario "{feature}" "{scenario_title}"')
def run_scenario(context: Context, feature: str, scenario_title: str):
    scenario: Scenario = load_scenario_from_feature_file(feature, scenario_title)
    context.execute_steps(scenario_to_txt(scenario))


@step('I run scenario "{feature}" "{scenario_title}" with data')
def run_scenario(context: Context, feature: str, scenario_title: str):
    scenario: Scenario = load_scenario_from_feature_file(feature, scenario_title)
    iterator = iter(context.table)
    # up to now, fail fast --> first failing row will interrupt the test
    scenario_has_failed = False
    try:
        while not scenario_has_failed:
            row = next(iterator)
            scenario_with_data: str = scenario_to_txt(scenario, row)
            try:
                context.execute_steps(scenario_with_data)

            except AssertionError as e:
                scenario_has_failed = True
                # context.scenario_data["error"] = e
    except StopIteration:
        pass
