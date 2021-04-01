import peewee
import playhouse.sqlite_ext as sqlite
from ._source import DataSource

db_proxy = peewee.DatabaseProxy()


class BaseModel(peewee.Model):
    class Meta:
        database = db_proxy

class Gene(BaseModel):
    name = peewee.CharField()
    oldid = peewee.IntegerField()
    v_vector = sqlite.JSONField()
    u_vector = sqlite.JSONField()
    si_vector = sqlite.JSONField()


class SqlLiteSource(DataSource):
    def __init__(self, file):
        self._db = sqlite.SqliteExtDatabase(file)
        db_proxy.initialize(self._db)

    def get_gene_ids(self, gene_set):
        pass
