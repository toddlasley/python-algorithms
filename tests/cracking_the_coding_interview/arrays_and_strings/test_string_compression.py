from algorithms.cracking_the_coding_interview.arrays_and_strings.string_compression import compress_string

def test_string_compression():
    assert compress_string('') == ''
    assert compress_string('abc') == 'abc'
    assert compress_string('abbc') == 'abbc'
    assert compress_string('aabc') == 'aabc'
    assert compress_string('abcc') == 'abcc'
    assert compress_string('aaabc') == 'aaabc'
    assert compress_string('aaabbbccc') == 'a3b3c3'
    assert compress_string('aaabbbbbccc') == 'a3b5c3'
