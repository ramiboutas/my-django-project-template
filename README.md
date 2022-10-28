# my-django-project-template
 This a base template I want to use for my Django projects


## Features

- Django to do: create a release 4.1 https://www.toolsqa.com/git/github-releases/
- pip-tools
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- __PostgreSQL__ database support with psycopg2.
- __python-dotenv__. Why python-dotenv instead of django-dotenv? One simple reason: django-dotenv has more methods and more complete.



## Set up 

### Create and activate the virtual environment (venv)

Creating the venv on __Unix systems__:
``python3 -m venv venv``

And on __Windows__:
``python -m venv venv``


Activating it on __Unix systems__:
``source venv/bin/activate``


And on __Windows__ by using:
* PowerShell: ``venv\\Scripts\\activate.bat``
* or CMD: ``venv\\Scripts\\activate.ps1``


### Collecting packages inside the venv

``python -m pip install pip-tools``



