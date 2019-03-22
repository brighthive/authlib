"""Application configuration.

"""


class Config(object):
    """Configuration class.

    This class encapsulates all the necessary information needed by
    an OAuth 2.0 provider in order to validate a token.

    Args:
        provider (str): Name of the OAuth 2.0 provider.
        base_url (str): Base URL for the OAuth 2.0 provider.
        jwks_url (str): URL for the JSON web token keys.
        algorithms (list): Accepted JWT algorithms.
        audience (str): Audience (e.g O)


    """

    def __init__(self, provider: str, base_url: str, jwks_url: str, algorithms: list, audience: str = None):
        self.provider = provider
        self.base_url = base_url
        self.jwks_url = jwks_url
        self.algorithms = algorithms
        self.audience = audience
