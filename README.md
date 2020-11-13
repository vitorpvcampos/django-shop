# django-shop
## Shop application following the book _Django 3 by Example_

![Django CI](https://github.com/vitorpvcampos/django-shop/workflows/Django%20CI/badge.svg)
[![Updates](https://pyup.io/repos/github/vitorpvcampos/django-shop/shield.svg)](https://pyup.io/repos/github/vitorpvcampos/django-shop/)
[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![Django 3.1](https://img.shields.io/badge/django-3.1-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/vitorpvcampos/django-shop/blob/master/LICENSE)

### How to run the project?

* Clone the repository
* Create a virtual environment
* Install the dependencies
* Run the migrations

```
git clone https://github.com/vitorpvcampos/django-shop.git
cd django-shop
pip install pipenv
pipenv install --dev
python manage.py migrate

```

#### PEP8 lint
```
pipenv run flake8
```
