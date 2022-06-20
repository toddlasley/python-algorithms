from algorithms.leet_code.easy.is_isomorphic import is_isomorphic

def test_is_isomorphic():
    assert is_isomorphic('egg', 'add')
    assert not is_isomorphic('foo', 'bar')
    assert is_isomorphic('paper', 'title')
    assert not is_isomorphic('badc', 'baba')
