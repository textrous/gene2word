__version__ = "2.0.0a0"

import abc, functools, numpy as np
from ._source import DataSource
from ._sqlite import SqliteSource


class Translator(abc.ABC):
    def __init__(self, data_source):
        self.data_source = data_source

    def translate(self, gene_set):
        V = self.data_source.get_gene_matrix(gene_set).sum(axis=0)
        U = self.data_source.get_word_matrix()
        return V, U

@functools.cache
def get_translator(db="g2w.db"):
    source = SqliteSource(db)
    return Translator(source)

def translate(gene_set):
    return get_translator().translate(gene_set)
