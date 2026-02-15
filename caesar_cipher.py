
"""
Function for caesar_cipher.
"""

def shift_text(text: str, shift: int) -> str:
    """
        Common function to shift alphabetical characters in the text.
        Positive shift is used for encryption and negative shift for decryption.
    """
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,.<>/?"
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch in digits:
            result += digits[(digits.index(ch) + shift) % 10]
        elif ch in symbols:
            result += symbols[(symbols.index(ch) + shift) % len(symbols)]
        else:
            result += ch

    return result

def encrypt_caesar(text: str, shift: int) -> str:
    """
        Encrypts the input text using Caesar cipher.

        Each letter in the plaintext is shifted forward in the alphabet by the specified number of positions.
         Non-alphabetic characters are not changed.
    """
    return shift_text(text, shift)


def decrypt_caesar(text: str, shift: int) -> str:
    """
        Decrypts the encrypted text using Caesar cipher.

        The Caesar cipher shifts each alphabetic character in the plaintext by a fixed number of positions.
        This function reverses that shift to retrieve the original message.
    """
    return shift_text(text, -shift)


if __name__ == "__main__":
    encrypted = encrypt_caesar("HELLO 123!@", 2)
    print("Encrypted:", encrypted)
    decrypted = decrypt_caesar(encrypted, 2)
    print("Decrypted:", decrypted)