from algorithms.leet_code.easy.integer_palindrome import is_palindrome

def test_integer_palindrome():
    assert is_palindrome(1)
    assert not is_palindrome(-1)
    assert is_palindrome(12321)
    assert not is_palindrome(12323)
    assert not is_palindrome(12345678)
    assert is_palindrome(12344321)
    assert not is_palindrome(10)
    assert is_palindrome(99)
    assert not is_palindrome(100)
