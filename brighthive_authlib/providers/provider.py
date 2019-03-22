"""OAuth 2.0 Provider Base Class

This class is the base class for all OAuth 2.0 providers supported by the
libray.

"""

import os
from brighthive_authlib.config import Config


class OAuth2Provider(object):
    """OAuth 2.0 Provider Base Class.

 self.provider = provider
        self.base_url = base_url
        self.jwks_url = jwks_url
        self.algorithms = algorithms
        self.audience = audience

    """

    __slots__ = ['provider', 'base_url', 'jwks_url', 'algorithms', 'audience']

    def __init__(self):
        self.provider = None
        self.base_url = None
        self.jwks_url = None
        self.algorithms = None
        self.audience = None

    def from_object(self, obj: Config):
        """Configure the library from a configuration object.

        Args:
            obj (Config): A configuration object to pull configurations from.

        """

        self.provider = obj.provider
        self.base_url = obj.base_url
        self.jwks_url = obj.jwks_url
        self.algorithms = obj.algorithms
        self.audience = obj.audience

    def from_env(self):
        """Configure the library from the OS environemt."""

        self.provider = os.getenv('OAUTH2_PROVIDER', None)
        self.base_url = os.getenv('OAUTH2_BASE_URL', None)
        self.jwks_url = os.getenv('OAUTH2_JWKS_URL', None)
        self.algorithms = os.getenv('OAUTH2_ALGORITHMS', None)
        self.audience = os.getenv('OAUTH2_AUDIENCE', None)
