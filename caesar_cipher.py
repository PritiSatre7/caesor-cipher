
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

def decrypt_caesar(text: str, shift: int) -> str:
    """
    Decrypts a text that was encrypted using the Caesar Cipher technique.

    Each alphabetical character in the input text is shifted backward
    by the giving shift value and Non-alphabetical characters remain unchanged.

    :param text: The encrypted text to be decrypted
    :param shift: The number of positions used during encryption
    :return: The decrypted plain text
    """
    decrypted = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += ch

    return decrypted


if __name__ == "__main__":
    print(encrypt_caesar("Hello", 2))
