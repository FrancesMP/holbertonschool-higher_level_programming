#!/usr/bin/python3
"""
Print the lowercase alphabet, excluding the letters 'e' and 'q'.
This script uses a for loop to iterate through ASCII codes of lowercase letters (97-122)
and skips characters corresponding to 'e' (code 101) and 'q' (code 113).
"""
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
