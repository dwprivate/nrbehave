import csv
import glob

from _steps.common import load_scenario_from_feature_file, scenario_to_txt
from behave import *
from behave.model import Examples, Feature, Row, Scenario, Table
from behave.parser import parse_file
from behave.runner import Context


@step('a csv file "{file}" with encoding "{encoding}"')
def step_impl(context, file, encoding):
    # up to now, generate a list. Could be improved
    with open(
        "data/FSMH.SRP.WFI121.FFILTRE.csv", newline="", encoding="latin-1"
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        datatable = Table(reader.fieldnames)
        Table

        for row in reader:
            # stripped_row = {key: value.strip() for key, value in row.items()}
            row = Row(reader.fieldnames, [cell.strip() for cell in list(row.values())])
            datatable.add_row(row)
    context.scenario_data["datatable"] = datatable


@step('a scenario outline "{feature}" "{title}"')
def step_impl(context, feature, title):
    context.scenario_data["outline"] = load_scenario_from_feature_file(feature, title)


@step("check all CSV rows")
def step_impl(context: Context):
    for row in context.scenario_data["datatable"]:
        parsed_scenario = scenario_to_txt(context.scenario_data["outline"], row)
        context.execute_steps(parsed_scenario)
