__version__ = "2.0.0a0"

import abc
from ._source import DataSource
from ._sqlite import SqlLiteSource

class Translator(abc.ABC):
    def __init__(self, data_source):
        self.data_source = data_source
