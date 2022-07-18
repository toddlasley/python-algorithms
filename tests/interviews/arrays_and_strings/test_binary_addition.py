from algorithms.interviews.arrays_and_strings.binary_addition import binary_addition

def test_binary_addition():
    assert binary_addition('11', '1') == '100'
    assert binary_addition('1', '11') == '100'
    assert binary_addition('11', '11') == '110'
    assert binary_addition('111', '111') == '1110'
    assert binary_addition('111', '1') == '1000'
    assert binary_addition('1', '111') == '1000'
    assert binary_addition('000001', '000001') == '000010'
    assert binary_addition('1010101', '101010') == '1111111'
    assert binary_addition('0', '0') == '0'
    assert binary_addition('00', '00') == '00'
    assert binary_addition('000', '000') == '000'
    assert binary_addition('000', '0') == '000'
    assert binary_addition('00', '0') == '00'
    assert binary_addition('0', '000') == '000'
    assert binary_addition('0', '00') == '00'
