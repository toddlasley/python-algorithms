from algorithms.leet_code.medium.zig_zag_conversion import zig_zag_conversion

def test_zig_zag_conversion():
    assert zig_zag_conversion('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert zig_zag_conversion('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert zig_zag_conversion('PAYPALISHIRING', 2) == 'PYAIHRNAPLSIIG'
    assert zig_zag_conversion('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
