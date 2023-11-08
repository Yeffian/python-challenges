def encrypt(text, shift_value):
    result = ""
 
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) + shift_value - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift_value - 97) % 26 + 97)
 
    return result

def decrypt(text, shift_value):
    return encrypt(text, 26 - shift_value)
