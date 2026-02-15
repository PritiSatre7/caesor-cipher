
"""
Function for caesar_cipher.
"""

def shift_text(text: str, shift: int) -> str:
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


def encrypt_caesar(text: str, shift: int) -> str:
    return shift_text(text, shift)


def decrypt_caesar(text: str, shift: int) -> str:
    return shift_text(text, -shift)


if __name__ == "__main__":
    encrypted = encrypt_caesar("HELLO", 2)
    print(encrypted)
    print(decrypt_caesar(encrypted, 2))
