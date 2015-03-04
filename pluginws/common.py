from flask import jsonify
from flask_classy import FlaskView
import logging


# Define Base Class
class DashPlugin(FlaskView):
    """The base class for all dashboard plugins. Plugins provide
    functionality by defining a subclass of DashPlugins and overriding
    the abstract methods defined here.
    """

    def __init__(self):
        self._base_route = self.__class__.__name__.lower()

        """The base variables that define the plugin"""
        self.author = ''
        self.version = ''
        self.description = ''

    def index(self):
        return jsonify(self._content())

    def _content(self):
        """Returns should return a dict containing all the information that
        should be returned when a call to the api is made
        """
        return ()

