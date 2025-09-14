# Write your solution to exercise 2 here
from string import ascii_lowercase #abcdefghijklmnopqrstuvwxyz

def caesar_encrypt(text: str, shift_value: int):
    encrpted_string = ""
    #print(ascii_lowercase)
    #print(text, shift_value)

    for char in text:
        char_index = ascii_lowercase.find(char)                 #Find the index of current char from input text
        encrpt_char_index = char_index+shift_value              #Find encryption char index by shifting right with input shift value

        if encrpt_char_index >= len(ascii_lowercase):           #if encryption char index reached end of lower case chars, move index back to beginning 
            encrpt_char_index-=len(ascii_lowercase)

        encrpted_string+=ascii_lowercase[encrpt_char_index]     #Append the new char to encrypted string

    return encrpted_string

def caesar_decrypt(text: str, shift_value: int):
    decrypted_string = ""

    for char in text:
        char_index = ascii_lowercase.find(char)                 #Find the index of current char from input text
        decrypt_char_index = char_index-shift_value             #Find encryption char index by shifting left with input shift value

        if decrypt_char_index < 0:                              #if encryption char index crossed 0, move index back to end 
            decrypt_char_index+=len(ascii_lowercase)

        decrypted_string+=ascii_lowercase[decrypt_char_index]   #Append the new char to decrypted string

    return decrypted_string


def encrypt_test():
    words_to_encrypt = [
    "one",
    "of",
    "the",
    "foods",
    "i",
    "like",
    "is",
    "pizza"
    ]

    for word in words_to_encrypt:
        encrypted = caesar_encrypt(word, 3)
        print(encrypted)

#encrypt_test()

def decrypt_test():
    secret_message = [
    "ersxliv", 
    "sri", 
    "mw", 
    "qegevsrm", 
    "gewwivspi", 
    "figeywi", 
    "mx", 
    "mw", 
    "gliet", 
    ]

    for word in secret_message:
        decrypted = caesar_decrypt(word, 4)
        print(decrypted)

#decrypt_test()

def encrypt_decrypt_test():
    ecrypt_and_decrypt = [
    "message",
    "encrypted",
    "and",
    "decrypted"
    ]
    # Becaues the encryption is decrypted with the same shift value as it was encrypted, all the prints are True
    for word in ecrypt_and_decrypt:
        encrypted = caesar_encrypt(word, 15)
        decrypted = caesar_decrypt(encrypted, 15)
        print(word == decrypted)

    # Test the encryption with 26 as the shift value
    # The words should not change because the shift value is the same as the alphabet length

    for word in ecrypt_and_decrypt:
        encrypted = caesar_encrypt(word, 26)
        decrypted = caesar_decrypt(word, 26)
        print(word == encrypted == decrypted)

#encrypt_decrypt_test()