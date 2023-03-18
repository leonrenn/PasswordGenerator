"""
Exceptions for the main program.
"""


class WrongFromatParserArgument(Exception):
    """Raised when the argument to the number 
    of charaters is in the wrong format.
    """
    pass


class NoPasswordSpecification(Exception):
    """Raised when no password specification
    on the type of characters is given.
    """
    pass
