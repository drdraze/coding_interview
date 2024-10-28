##### Task: Given a list of strings, group them in groups of xor cipher equivalence. 

Two strings are xor cipher equivalent if they are an encryption of each other using the xor cipher. The XOR cipher converts each characted in a string to binary representation, performs the XOR operation bitwise between the same binary representation of the encryption key and the string.

Example: ["hello", "jgnnm", "`{g", "ec{", "h", "bye", "gay", "kfool" ,"a"] --> [['hello', 'kfool], ['`{g', 'bye'], ['ec{', 'gay'], ['h'], ['a']]

Hint: `ord()` returns the Unicode code point for a one-character string
