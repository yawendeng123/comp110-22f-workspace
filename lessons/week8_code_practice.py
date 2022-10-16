"""Code Writing Practice."""


def zip(ks: list[str], vs: list[str]) -> dict[str, str]:
    """Build a dictionary from two lists."""
    assert len(ks) == len(vs)
    result: dict[str, str] = {}
    for i in range(0, len(ks)):
        result[ks[i]] = vs[i]
    return result

    # if we use while loop
    # i: int = 0
    # while i < len(ks):
        # result[ks[i]] = vs[i]
    # return result