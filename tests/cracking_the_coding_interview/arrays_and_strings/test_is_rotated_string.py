from algorithms.cracking_the_coding_interview.arrays_and_strings.is_rotated_string import is_rotated_string

def test_is_rotated_string():
    assert is_rotated_string('waterbottle', 'erbottlewat')
    assert is_rotated_string('test', 'test')
    assert not is_rotated_string('waterbottle', 'erbotthewat')
    assert not is_rotated_string('asdf', 'asdff')
