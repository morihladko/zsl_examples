"""

"""
from zsl import Zsl, inject
from zsl.application.modules.cli_module import ZslCli
from zsl.application.containers.web_container import WebContainer

from db.install import install as install_db
import time_tracker


@inject(cli_=ZslCli)
def cli(cli_: ZslCli):
    cli_.cli()

app = Zsl(time_tracker.app_name,
          version=time_tracker.__version__,
          modules=WebContainer.modules())

install_db()


if __name__ == "__main__":
    app.run_web(port=5001)
