from algorithms.cracking_the_coding_interview.arrays_and_strings.is_permutation import is_permutation

def test_is_permutation():
    assert is_permutation('', '')
    assert not is_permutation('', 'a')
    assert is_permutation('asdf', 'asdf')
    assert is_permutation('asdf', 'dsaf')
    assert not is_permutation('asd', 'asdf')
    assert not is_permutation('asdf', 'dsgf')
    assert is_permutation('asdfg', 'gadfs')
    assert not is_permutation('asdfg', 'ga2fs')
