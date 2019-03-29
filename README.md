# BrightHive Auth Library

Authlib is a library built specifically for simplifying the task of adding authentication and authorization features to RESTful web services that reside within BrightHive Data Trusts. With this library, developers simply need to provision an OAuth 2.0 provider and inject it into a simple decorator to protect specific URLs.

## Quick Links

- [Read the docs](http://brighthive-auth-service.docs.io)

## Features

- Support for Auth0.
- Simple decorator for injecting auth capabilities into applications.
- Purpose-built for use with [Flask](http://flask.pocoo.org/) applications, however can be extended to other frameworks.

## Installation

### PyPi

[Pypi](https://pypi.org) is the fastest method for installing this library. Simply install the `brighthive-authlib` package via the Pip installer. This library is intended for use with Python 3.5+.

```bash
pip install brighthive-authlib
```

### Dependencies

- flask >= 1.0.2
- pycryptodome >= 3.8.0
- python-jose[pycryptodome] >= 3.0.1
- requests >= 2.21.0

## Source Code
