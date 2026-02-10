"""

Function for caesar_cipher.
"""

def encrypt_caesar(text, shift):
    if text == "":
        return ""
    else:
        return chr(ord(text[0]) + shift) + encrypt_caesar(text[1:], shift)


if __name__ == "__main__":
    print(encrypt_caesar("Hello", 2))
