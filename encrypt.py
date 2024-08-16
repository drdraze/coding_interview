class CaesarCipher:
    def encode(self, string, d):
        """Encodes string using caesar shift of d characters"""
        encrypted = ""
        for char in string:
            encrypted += chr((ord(char) + d - ord("a")) % 26 + ord("a"))
        return encrypted

    def _char_distance(self, char1, char2):
        return (ord(char1) - ord(char2)) % 26
