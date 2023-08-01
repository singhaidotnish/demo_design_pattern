"""
Bot context: A python object to hold the show and shot
information
"""

# Local imports
from .exceptions import InvalidContextError


class BotContext(object):
    """A object to hold the show and/or the shot a user is currently
    working on
    """

    def __init__(self, show, shot=None):
        """BotContext initializer

        Args:
            show (str): the name of the show
            shot (str): the name of the shot. Optional defaults to None
        """
        super(BotContext, self).__init__()
        self.__show = show
        self.__shot = shot

    ##########################################################################
    # Properties
    ##########################################################################
    @property
    def show(self):
        """Gets the show name"""
        return self.__show

    @property
    def shot(self):
        """Gets the shot name"""
        return self.__shot

    ##########################################################################
    # Methods
    ##########################################################################
    def as_dict(self):
        """Returns BotContext as dictionary

        Returns:
            dict
        """
        ctx = {'show': self.__show}

        if self.__shot is not None:
            ctx['shot'] = self.__shot

        return ctx

    def validate(self):
        """Checks if the context is valid

        Raises:
            InvalidContextError
        """
        if not self.__show:
            raise InvalidContextError("Invalid show name: `{0}`".format(
                self.__show))

        if not isinstance(self.__show, basestring):
            raise InvalidContextError(
                "Show name: `{0}`. Expected string. But found `{1}`".format(
                    self.__show, type(self.__show)))

        if self.__shot and not isinstance(self.__shot, basestring):
            raise InvalidContextError(
                "Shot name: `{0}`. Expected string. But found `{1}`".format(
                    self.__shot, type(self.__shot)))

    def is_valid(self):
        """Checks if the context is valid

        Returns:
            boolean
        """
        try:
            self.validate()
        except InvalidContextError:
            return False
        else:
            return True
