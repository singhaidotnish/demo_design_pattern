"""Custom exceptions"""


class BotException(Exception):
    """A base exception for all bot specific errors"""


class InvalidContextError(BotException):
    """Exception raised when context is invalid"""

class YAMLResolveError(BotException):
    """Exception raised while resolving a config file"""