from util.configs import build_classifier_function_config
from util.enums import State
from . import _template, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=_template,
        input_example=INPUT_EXAMPLE,
        issue_id=-1,  # you need to look this up in the issues https://github.com/code-kern-ai/bricks/issues
        tabler_icon="Template",  # Add any fitting icon from tabler-icons.io
        min_refinery_version="x.x.x",
        state=State.DRAFT,  # in the actual module, set this to PUBLIC before pushing to main!
    )