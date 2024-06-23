import csv

from _steps.common import load_scenario_from_feature_file, scenario_to_txt
from behave.model import *

if __name__ == "__main__":

    scenario: Scenario = load_scenario_from_feature_file(feature, scenario_title)

    with open(
        "data/FSMH.SRP.WFI121.FFILTRE.csv", newline="", encoding="latin-1"
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        print(reader.fieldnames)
        for row in reader:
            stripped_row = {key: value.strip() for key, value in row.items()}
            print(stripped_row)
