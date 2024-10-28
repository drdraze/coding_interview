from encrypt import XORCipher


class TestCaesarCipher:
    def test_encode(self):
        test_object = XORCipher()
        assert test_object.encode("gsk", 2) == "eqi"
