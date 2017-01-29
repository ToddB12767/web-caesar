#encrypt message function
def encrypt(msg, rot):

    encrypted = []
    rot = int(rot)

    for letter in msg:
        if letter.isalpha():
            encrypted.append(rotate_character(letter,rot))
        else:
            encrypted.append(letter)
    return ''.join(encrypted)

# Aplabet position function
def alphabet_position(letter):
    if len(letter) != 1:
        return 0
    new = ord(letter)
    if 65 <= new <= 90:
        # Upper case letter
        return new - 65
    elif 97 <= new <= 122:
        # Lower case letter
        return new - 97
    # Unrecognized character
    return 0

# Rotate character function
def rotate_character(char, rot):
    shift = 97 if char.islower() else 65
    return chr((ord(char) + rot - shift) % 26 + shift)
