import os, sys, pickle, numpy as np
from gene2word import SqliteSource

source = SqliteSource("test.db")

if "genes" in sys.argv:
    print("Unpickling genes")
    genes = pickle.load(open("gene2word/gene2id.pkl", "rb"))
    V = pickle.load(open("gene2word/V.pkl", "rb"))
    genes = dict(sorted(genes.items(), key=lambda kv: kv[1]))
    # Assert that data starts at 0, increases incrementally and that for each gene there
    # is a corresponding vector in V.
    assert list(genes.values())[0] == 0
    assert all(np.diff(list(genes.values())) == 1)
    assert len(genes) == len(V)
    print("Importing genes")
    source.import_genes(genes.keys(), V)

if "words" in sys.argv:
    print("Unpickling words")
    words = pickle.load(open("gene2word/id2word.pkl", "rb"))
    U = pickle.load(open("gene2word/U.pkl", "rb"))
    words = dict(sorted(words.items(), key=lambda kv: kv[0]))
    # Assert that data starts at 0, increases incrementally and that for each word there
    # is a corresponding vector in U.
    assert list(words.keys())[0] == 0
    assert all(np.diff(list(words.keys())) == 1)
    assert len(words) == len(U)
    print("Importing words")
    source.import_words(words.values(), U)
