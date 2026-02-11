## Caesar Cipher

### Description
Character Encryption is a simple technique used to secure text by modifying each character using a fixed key value.
In this method, encryption is done by adding the key value to each character, while decryption is done by subtracting the same key value. 
This technique is known as the Caesar.

### Features
Easy to understand and implement .
Uses basic addition and subtraction.
Works on alphabetical characters.
Fast and efficient.
Suitable for beginners.


### Working
1.Encryption (Using Addition)
Each character in the plain text is shifted forward by 2 using addition.
```
Encrypted Example:
H + 2 → J
E + 2 → G
L + 2 → N
L + 2 → N
O + 2 → Q
Encrypted Character = Original Character + 2
```
###Encryption output
Input: HELLO  
Shift: 2 
Output: JGNNQ

2.Decryption (Using Subtraction)
Each encrypted character is shifted backward by 2 using subtraction.
```
Decryption Example
J − 2 → H
G − 2 → E
N − 2 → L
N − 2 → L
Q − 2 → O
Decrypted Character = Encrypted Character − 2
```
Decryption output
Input: JGNNQ  
Shift: 2 
Output: HELLO

```
Final Output
Encrypted Text: JGNNQ
Decrypted Text: HELLO
```
