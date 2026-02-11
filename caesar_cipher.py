def encrypt_caesar(text : str , shift: int) -> str:
    pass

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
    text = "JGNNQ"
    shift = 2
    print("Decrypted Output:", decrypt_caesar(text, shift))
