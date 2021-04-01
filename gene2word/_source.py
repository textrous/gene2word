import abc

class DataSource(abc.ABC):
    @abc.abstractmethod
    def get_gene_ids(self, gene_set):
        pass
