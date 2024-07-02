from behave import *

from nrbehave.utils.virtel import VirtelEmulator


@then(
    'la zone "langue" {row:d},{col:d} correspond à l\'initiale de la valeur "{value}"'
)
def step_impl(context, row: int, col: int, value: str, name: str = "langue"):
    assert VirtelEmulator(context).string_get(row, col).strip()[0:1] == value.strip()
