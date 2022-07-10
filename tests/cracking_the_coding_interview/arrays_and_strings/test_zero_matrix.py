from algorithms.cracking_the_coding_interview.arrays_and_strings.zero_matrix import zero_matrix

def test_zero_matrix():
    a = [[1], [1]]
    a_expected = [[1], [1]]
    b = [[1, 1], [1, 1]]
    b_expected = [[1, 1], [1, 1]]
    c = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    c_expected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    d = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    d_expected = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    e = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    e_expected = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    f =  [[0], [1]]
    f_expected =  [[0], [0]]
    g = [[1, 0], [1, 1]]
    g_expected = [[0, 0], [1, 0]]
    h = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    h_expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    i = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1]]
    i_expected = [[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0]]
    j = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    j_expected = [[1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0]]

    zero_matrix(a)
    assert a == a_expected
    zero_matrix(b)
    assert b == b_expected
    zero_matrix(c)
    assert c == c_expected
    zero_matrix(d)
    assert d == d_expected
    zero_matrix(e)
    assert e == e_expected
    zero_matrix(f)
    assert f == f_expected
    zero_matrix(g)
    assert g == g_expected
    zero_matrix(h)
    assert h == h_expected
    zero_matrix(i)
    assert i == i_expected
    zero_matrix(j)
    assert j == j_expected
