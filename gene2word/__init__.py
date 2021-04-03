__version__ = "2.0.0a0"

import abc, functools, numpy as np
from ._source import DataSource
from ._sqlite import SqliteSource


class Translator(abc.ABC):
    def __init__(self, data_source):
        self.data_source = data_source

    def translate(self, gene_set):
        from sklearn.metrics.pairwise import cosine_similarity

        V = self.data_source.get_gene_matrix(gene_set).sum(axis=0)
        U = self.data_source.get_word_matrix()
        cos = cosine_similarity(V.reshape(1, -1), U)[0]
        similars = np.argsort(-cos)
        words = self.data_source.get_all_words()
        return dict(zip(words[similars], cos[similars]))


@functools.cache
def get_translator(db=os.path.abspath("./g2w.db")):
    if not os.path.exists(db):
        raise MissingSourceError("Could not open source file '%source%'.", source)
    source = SqliteSource(db)
    return Translator(source)


def translate(gene_set):
    return get_translator().translate(gene_set)
