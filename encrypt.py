class XORCipher:
    def encode(self, string, key):
        """Encodes string using caesar shift of d characters"""
        return "".join(chr(ord(c) ^ key) for c in string)
