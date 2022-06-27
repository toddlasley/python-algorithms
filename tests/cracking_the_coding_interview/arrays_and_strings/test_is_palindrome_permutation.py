from algorithms.cracking_the_coding_interview.arrays_and_strings.is_palindrome_permutation import is_palindrome_permutation

def test_is_palindrome_permutation():
    assert is_palindrome_permutation('taco cat')
    assert is_palindrome_permutation('toct aac')
    assert not is_palindrome_permutation('togt aac')
    assert is_palindrome_permutation('asdffdsa')
    assert is_palindrome_permutation('fsdafdsa')
