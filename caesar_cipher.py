def encrypt_caesar(text : str , shift: int) -> str:
    pass

def decrypt_caesar(text: str, shift: int) -> str:
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
