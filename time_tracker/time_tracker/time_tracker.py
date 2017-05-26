from zsl import Zsl, inject
from zsl.application.modules.cli_module import ZslCli
from zsl.application.containers.web_container import WebContainer

from db.install import install as install_db


@inject(cli_=ZslCli)
def cli(cli_: ZslCli):
    cli_.cli()

app = Zsl(__name__, modules=WebContainer.modules())

install_db()

