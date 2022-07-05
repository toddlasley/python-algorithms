from algorithms.leet_code.medium.next_permutation import next_permutation

def test_next_permutation():
    a = []
    next_permutation(a)
    assert a == []

    b = [1]
    next_permutation(b)
    assert b == [1]

    c = [1, 2]
    next_permutation(c)
    assert c == [2, 1]

    d = [2, 1]
    next_permutation(d)
    assert d == [1, 2]

    e = [1, 2, 3]
    next_permutation(e)
    assert e == [1, 3, 2]

    f = [1, 2, 3, 4, 5, 6]
    next_permutation(f)
    assert f == [1, 2, 3, 4, 6, 5]

    g = [6, 5, 4, 3, 2, 1]
    next_permutation(g)
    assert g == [1, 2, 3, 4, 5, 6]

    h = [1, 4, 5, 6, 2, 3]
    next_permutation(h)
    assert h == [1, 4, 5, 6, 3, 2]

    i = [1, 6, 5, 4, 3, 2]
    next_permutation(i)
    assert i == [2, 1, 3, 4, 5, 6]
