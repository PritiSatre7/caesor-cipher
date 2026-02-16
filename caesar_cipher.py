
"""
Function for caesar_cipher.
This function provides the encrypt and decrypt text using the Caesar cipher.
Supports uppercase letters, lowercase letters, digits, and symbols.
"""

def shift_text(text: str, shift: int) -> str:
    """
        Shift characters in the input text by a specified amount.

        This function handles: Uppercase letters (A-Z)
                               Lowercase letters (a-z)
                               Digits (0-9)
                               Symbols (!@#$%^&*()_+-=[]{};:,.<>/?)
                               Other characters (e.g., spaces, tabs)

        Parameters:text (str): Input string to be shifted.
                   shift (int): Number of positions to shift characters.
                   Positive shift for encryption, negative for decryption.

        Returns:str: The resulting string after shifting all supported characters.

         Example:
                 >>> shift_text("Hello 123!", 2)
                 'Jgnnq 345!'
                 >>> shift_text("Jgnnq 345!", -2)
                 'Hello 123!'
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
        Encrypt text using Caesar cipher.

        Parameters: text (str): Plaintext to encrypt.
                    shift (int): Number of positions to shift characters forward.

        Returns: str: Encrypted text

        Example:
                >>> encrypt_caesar("HELLO 123!@", 2)
                'JGNNQ 345#$'
    """
    return shift_text(text, shift)


def decrypt_caesar(text: str, shift: int) -> str:
    """
        Decrypt text encrypted with Caesar cipher.

        Parameters:text (str): Encrypted text.
                   shift (int): Number of positions originally used to shift characters.

        Returns: str: Decrypted (original) text.

        Example:
                >>> decrypt_caesar("JGNNQ 345#$", 2)
                'HELLO 123!@'
    """
    return shift_text(text, -shift)


if __name__ == "__main__":
    encrypted = encrypt_caesar("HELLO 123!@", 2)
    print("Encrypted:", encrypted)
    decrypted = decrypt_caesar(encrypted, 2)
    print("Decrypted:", decrypted)