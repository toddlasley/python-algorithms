from algorithms.cracking_the_coding_interview.arrays_and_strings.is_unique import is_unique

def test_is_unique():
    assert is_unique('')
    assert is_unique('a')
    assert not is_unique('aa')
    assert is_unique('ab')
    assert is_unique('abc')
    assert not is_unique('abca')
