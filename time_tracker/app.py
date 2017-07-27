from time_tracker.time_tracker import app
from zsl import inject

from zsl.application.modules.web.web_context_module import WebHandler


@inject(web_handler=WebHandler)
def run_web(web_handler):
    # type:(WebHandler)->None
    web_handler.run_web(port=5555)


if __name__ == "__main__":
    run_web()
