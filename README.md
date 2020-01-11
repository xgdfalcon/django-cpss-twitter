> ## 🛠 Status: In Development
> django-cpss-twitter currently in development.

# Python Twitter API - Django  [<img src="https://github.com/xgdfalcon/django-cpss-twitter/blob/master/twitter-django/static/cpss/logo.png?raw=true" alt="CPSS by XGDFalcon®" height="20px" />](https://controlpointsw.com) 

[![Build Status](https://travis-ci.org/xgdfalcon/django-cpss-twitter.svg?branch=master)](https://travis-ci.org/xgdfalcon/django-cpss-twitter)
[![PyPI version](https://badge.fury.io/py/django-cpss-twitter.svg)](https://badge.fury.io/py/django-cpss-twitter)

## Description

This is the [Django](https://www.djangoproject.com/) component of the
[Python Twitter Tools project](https://github.com/sixohsix/twitter),
it implements the needed functionality to integrate
[Python Twitter Tools](https://github.com/sixohsix/twitter)
in a Django based project.

## Django version

This project will focus on the currently supported Django releases as
stated on the [Django Project Supported Versions table](https://www.djangoproject.com/download/#supported-versions).

Backward compatibility with unsupported versions won't be enforced.

## Documentation

Project documentation is available at TBP.

## Setup

1. Add "django-cpss-twitter" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = [
        ...
        'twitter-django.CPSSTwitterConfig',
    ]
```
2. Include the django-cpss-twitter URLconf in your project urls.py like this::
```
    path('twitter/', include('django-cpss-twitter.urls')),
```
3. Run `python manage.py migrate` to create the django-cpss-twitter models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a client config (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/twitter/ 

## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) document for details.

## Versioning
This project follows [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

## License
This project follows the Apache license. See the [LICENSE](LICENSE) for details.

