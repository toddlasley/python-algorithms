from algorithms.cracking_the_coding_interview.arrays_and_strings.is_one_edit_away import is_one_edit_away

def test_is_one_edit_away():
    assert is_one_edit_away('asdf', 'asdf')
    assert is_one_edit_away('asdf', 'asd')
    assert is_one_edit_away('asdf', 'asdb')
    assert is_one_edit_away('asdf', 'asdfz')
    assert not is_one_edit_away('asdf', 'a')
    assert is_one_edit_away('', '')
    assert is_one_edit_away('', 'a')
    assert is_one_edit_away('a', '')
    assert not is_one_edit_away('asdf', 'as')
    assert not is_one_edit_away('asdf', 'ajkf')
    assert is_one_edit_away('abdf', 'asdf')
