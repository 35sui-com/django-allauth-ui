# AllAuth UI

UI templates for [django-allauth](https://github.com/pennersr/django-allauth)
built with Tailwind.

django-allauth is a great library, but the templates it provides out of the box
are minimal html. I usually end up re-designing the login / logout / signup
pages for each new Django project. This library aims at providing decent
defaults for new projects.

## Features

- Responsive design suitable for device sizes from mobile to desktop
- Styled social login themes
- Additional error information when [social logins fail](https://github.com/pennersr/django-allauth/issues/2142)

## Installation

```
pip install django-allauth-ui
```

Add django-allauth-ui **before** django-allauth in your INSTALLED_APPS. See
[./tests/settings.py](./tests/settings.py) for an example.

```python
INSTALLED_APPS = [
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
]
```

## Screenshots

![Log In](./images/signin.png)
![Sign Up](./images/signup.png)
![Password Reset](./images/password_reset.png)

## Generating screenshots

```
convert "$1" -crop 1072x901+436+200 crop_signin.png
```
