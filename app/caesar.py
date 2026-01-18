def caesar_cipher(plaintext: str, key: int) -> str:
    result = []

    key = key % 26

    for char in plaintext:
        if char.isupper():
            c = chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        elif char.islower():
            c = chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        else:
            c = char
        
        result.append(c)

    return "".join(result)






