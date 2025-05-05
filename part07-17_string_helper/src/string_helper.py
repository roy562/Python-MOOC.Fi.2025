# Write your solution here
from string import ascii_lowercase, ascii_uppercase, digits

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char in ascii_lowercase:
            new_string+=char.upper()
        elif char in ascii_uppercase:
            new_string+=char.lower()
        else:
            new_string+=char
    return new_string

def split_in_half(orig_string: str):
    total_chars = len(orig_string)
    half_index = total_chars//2
    return orig_string[:half_index],  orig_string[half_index:]

def remove_special_characters(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char in ascii_lowercase or char in ascii_uppercase or char in digits or char == " ":
            new_string+=char
            
    return new_string

#print(change_case("Well hello there!"))
#print(split_in_half("Well hello there!"))
#print(remove_special_characters("This is a test, lets see how it goes!!!11!"))