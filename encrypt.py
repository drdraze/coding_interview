class CaesarCipher:
    def encode(self, string, d):
        """Encodes string using caesar shift of d characters"""
        encrypted = ""
        for char in string:
            encrypted += chr((ord(char) + d - ord("a")) % 26 + ord("a"))
        return encrypted
