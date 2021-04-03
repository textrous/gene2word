import unittest, os
import gene2word as g2w

db_path = os.path.join(g2w._dirs.user_cache_dir, "g2w.db")


class TestG2W(unittest.TestCase):
    @unittest.skipIf(os.path.exists(db_path), "Skipped DB deploy, already deployed.")
    def test_001_first_use(self):
        with self.assertWarns(g2w.DeploymentWarning):
            g2w.translate(["SRSF3"])
