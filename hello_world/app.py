from zsl import Zsl, inject
from zsl.application.containers.web_container import WebContainer
from zsl.application.modules.cli_module import ZslCli
from zsl.application.modules.web.web_context_module import WebHandler
from zsl.task.task_decorator import json_output
from zsl.router import method


def create_and_run_app():
    app = Zsl('HelloWorld', modules=WebContainer.modules())

    @inject(zsl_cli=ZslCli)
    def run(zsl_cli: ZslCli) -> None:
            zsl_cli.cli()

    @method.route('/hello/<x>')
    @json_output
    def hello(x):
        return {"message": f"Hello World for {x}!"}

    run()


if __name__ == "__main__":
    create_and_run_app()

