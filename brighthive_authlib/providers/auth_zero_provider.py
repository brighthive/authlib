"""Auth0 OAuth 2.0 Provider.

Implementation of an Auth0 OAuth 2.0 Provier.

"""

from brighthive_authlib.providers import OAuth2Provider


class AuthZeroProvider(OAuth2Provider):
    """Auth0 OAuth 2.0 Provider."""

    def __init__(self):
        super().__init__()
