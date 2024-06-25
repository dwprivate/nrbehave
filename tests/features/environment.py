from _fixtures.selenium import environment as selenium_environment
from behave.runner import Context


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


def before_tag(context, tag):
    selenium_environment.before_tag(context, tag)


def after_tag(context, tag):
    selenium_environment.after_tag(context, tag)
