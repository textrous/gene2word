import unittest, os
import gene2word as g2w
import old.queryWord as qw


db_path = os.path.join(g2w._dirs.user_cache_dir, "g2w.db")
telomerase_geneset = [
    "SRSF3",
    "RPL12",
    "SRSF5",
    "HNRNPA1",
    "HNRNPA3",
    "LUC7L3",
    "RPL31",
    "RPL27A",
    "RPL10A",
    "DKC1",
    "SRSF6",
    "SRSF2",
    "ILF2",
    "KHSRP",
    "RPS5",
    "RBM8A",
    "U2AF2",
    "PCBP2",
]


class TestComparison(unittest.TestCase):
    def compare(self, f1, f2, *args, eq=None):  # pragma: nocover
        r1 = f1(*args)
        r2 = f2(*args)
        if eq is None:
            self.assertEqual(r1, r2)
        else:
            eq(r1, r2)

    def test_gene_set_translation(self):
        def comp_gst(translation, tuples):
            for (n1, v1), (n2, v2) in zip(translation.items(), tuples):
                self.assertEqual(n1, n2)
                self.assertAlmostEqual(v1, v2)

        self.compare(
            g2w.translate,
            lambda genes: qw.getWordVector(" ".join(genes), qw.U, qw.V, qw.SI),
            telomerase_geneset,
            eq=comp_gst,
        )
