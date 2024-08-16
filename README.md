##### Task: Given a list of strings, group them in groups of Caesar-equivalence. 

Two strings are Caesar-equivalent if they are a Caesar encryption of each other. Caesar encryption is one of the simplest encryption techniques where each letter is replaced by a letter some fixed shift down the alphabet. E.g., a shift of 3: A --> D, L --> O, Y --> B; a shift of -1: A --> Z, L --> K, Y --> X.
The strings "gsk" and "htl" are caesar equivalent.
The strings "gsk" and "ltl' are not.

Example: `['hello', 'dag', 'h', 'bye', 'gay', 'a'] --> [['hello'], ['dag', 'bye'], ['h', 'a'], ['gay']]`

Hint: `ord()` returns the Unicode code point for a one-character string