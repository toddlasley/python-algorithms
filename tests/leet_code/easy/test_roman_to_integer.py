from algorithms.leet_code.easy.roman_to_integer import roman_to_integer

def test_roman_to_integer():
    assert roman_to_integer('VI') == 6
    assert roman_to_integer('XVIII') == 18
    assert roman_to_integer('IX') == 9
    assert roman_to_integer('XLI') == 41