from behave.model import Scenario
from behave.runner import Context

from nrbehave.fixtures.selenium import environment as selenium_environment


# to move:
def embed(context: Context, data, title="", mime_type="text/plain"):
    print(title + "\n" + data)
    if isinstance(data, str):
        enc_data = f"{title}: {data}".encode()
        context.attach(mime_type, enc_data)
    # todo else

    for formatter in context._runner.formatters:
        if formatter.name == "html-pretty":
            print("to pretty")
            formatter.embed(mime_type=mime_type, data=data, caption=title)


def before_all(context):
    Context.embed = embed
    print("embed attached")


def after_all(context):
    print("after_all")


def before_scenario(context, scenario):
    context.scenario_data = {}


def after_scenario(context: Context, scenario: Scenario):
    print(f"Scenario {scenario.name} finished")
    print(context.captured.stdout)
    pass


def before_tag(context, tag):
    selenium_environment.before_tag(context, tag)


def after_tag(context, tag):
    selenium_environment.after_tag(context, tag)
