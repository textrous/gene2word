__version__ = "2.0.0a0"

import abc
from .queryWord import getWordVector


class Translator(abc.ABC):
    @abc.abstractmethod
    def get_gene_id(self, gene):
        pass
