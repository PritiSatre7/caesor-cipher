"""

Function for caesar_cipher.
"""

def encrypt_caesar(text, shift):
    """
    This Function encrypts the input text using caesar cipher.
    Each character is shifted by the given value.

    :param text: The input text to be encrypted.
    :param shift: Number of characters to shift.
    :return: Encrypted text.

    """

    if text == "":
        return ""
    else:
        return chr(ord(text[0]) + shift) + encrypt_caesar(text[1:], shift)


if __name__ == "__main__":
    print(encrypt_caesar("Hello", 2))
