VERSION = (0, 0, 1, "alpha", 1)


def get_version(version=None):
    v = VERSION if version is None else version
    assert len(v) == 5
    assert v[3] in ("alpha", "beta", "rc", "final")
    parts = 3
    main = ".".join(str(i) for i in v[:parts])
    sub = ""
    if v[3] != "final":
        mapping = {"alpha": "a", "beta": "b", "rc": "c"}
        sub = mapping[v[3]] + str(v[4])
    return main + sub


__version__ = get_version()
