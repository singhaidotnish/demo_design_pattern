"""Custom exceptions"""


class MyException(Exception):
    """A base exception for all bot specific errors"""


class InvalidContextError(MyException):
    """Exception raised when context is invalid"""


class YAMLError(MyException):
    """Exception raised while operating file"""
