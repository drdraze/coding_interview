from encrypt import CaesarCipher


class TestCaesarCipher:
    def test_encode(self):
        test_object = CaesarCipher()
        assert test_object.encode('gsk', d=1) == 'htl'
