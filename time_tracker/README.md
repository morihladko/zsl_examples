# First steps creating a ZSL app

ZSL is a small library for creating modern server applications able to merge  

## Time Tracker

In this tutorial we will create a small time tracking application  with an API 
endpoint and an admin interface with help of admin-on-rest. We will use 
SQLAlchemy to define our persisent storage

### Installing ZSL  

The easiest way to use ZSL is installing it trough [pip](https://pip.pypa.io/)
in a virtual environment. We will use Python 3 build in [venv](https://docs.python.org/3/library/venv.html),
but it will work with any other virtual env implementation.   

```bash
$ python -m venv ./env
$ source ./env/bin/activate
(env) $ pip install zsl
```

From this point forward all the scripts are run within this virtual environment.

### Creating a runner

Before we start to build our application is good to have a script to run it 
from the start. We will use Flask build-in server which can be included with 
ZSL's WebContainer.

```python
# ./app.py
from zsl import Zsl
from zsl.application.containers.web_container import WebContainer

app = Zsl(__name__, modules=WebContainer.modules())

if __name__ == '__main__':
    app.run_web()
```

### Settings

To run ZSL, we need setting package named `settings.default_settings` where 
we will put common settings. Later we will add a way to customize settings 
per installation. More on settings is in documentation in [Configuration](https://zsl.readthedocs.io/en/latest/configuration.html)
.

```bash
$ mkdir settings
$ touch settings/__init__.py
$ touch settings/default_settings.py
```

### Web app

To start the web server we just run the `app.py`.

```bash
$ python app.py
```

Now we can connect to it. For this tutorial we will use [HTTPie](https://httpie.org/)
tool as a http console client for its simpler and more developer oriented 
interface. You can of course use [curl](https://curl.haxx.se/) or any other 
console or GUI client.

```bash
$ http localhost:5000
HTTP/1.0 404 NOT FOUND
Content-Length: 38
Content-Type: text/html; charset=utf-8
Server: Werkzeug/0.12.2 Python/3.6.1

404 Not Found: path '' was not mapped.
```

The server is running and telling us it has nothing to show to us.
 
### Build in zsl.tasks

ZSL includes some simple tasks which can be included and are a good way to 
test our configuration. We define the variable `TASK_PACKAGES`, where we 
can list task packages as a tuple. What **task** are how to write them will 
be get shortly. 

```python
# settings/default_settings.py
TASK_PACKAGES = ('zsl.tasks',)
```

With `Ctrl^c` we kill our running `app.py` and after we start it again we 
can ask our app something useful.

```bash
$ http localhost:5000/task/zsl/version_task
HTTP/1.0 200 OK
Content-Length: 41
Content-Type: application/json
Server: Werkzeug/0.12.2 Python/3.6.1
ZSL-Flask-Layer: 0.15.3

{
    "ASL": "0.15.3",
    "SqlAlchemy": "1.1.10"
}
```

### Settings customization 

One thing we can notice using the web server script is that we don't have any
output what is happening and we have to restart it after every change. This 
is good for production environment, but during development and testing it 
would be nice to set different logging settings and enable debug options.

In ZSL this is done trough `*.cfg` files, which can override settings from 
`settings.default_settings`. To load an `*.cfg` file we define an environment
variable [ZSL_SETTINGS](https://zsl.readthedocs.io/en/latest/configuration.html#environment-variables). 

```bash
$ export ZSL_SETTINGS=`pwd`/settings/devel_settings.cfg
```

With that we can configure a console logger and we will set DEBUG mode for 
flask. More about these settings can be found in documentation in 
[Configuration, optional-fields](https://zsl.readthedocs.io/en/latest/configuration.html#optional-fields)
.

```python
# settings/devel_settings.cfg
LOG_HANDLERS = {
    'console': {
        'class': 'logging.StreamHandler'
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    }
}

DEBUG = True
RELOAD = True
``` 

Now after we kill and star our app again we can see what is happening inside 
our application.

```bash
$ python app.py
Injector configuration [...].
Initializing project external libraries.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Writing the application

Finally after little bit of set up we can start coding our application.

### Application package

We create our application as a python package, which can be easily used in 
another contexts. This improves interoperability and enables growing our app 
into more complex application.

```bash
$ mkdir time_tracker
$ touch time_tacker/__init__.py
```


```python
# time_tracker/__init__.py
app_name = 'time_tracker'

__version__ = 1.0
```
