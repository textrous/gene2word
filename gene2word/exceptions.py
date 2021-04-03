from errr.tree import make_tree as _t, exception as _e

_t(globals(),
    Gene2WordError=_e(
        MissingSourceError=_e("source"),
    )
)
