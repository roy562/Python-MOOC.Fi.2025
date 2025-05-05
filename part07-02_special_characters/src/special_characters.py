# Write your solution here
import string

def separate_characters(text:str):
    string1 = ""
    string2 = ""
    string3 = ""

    for char in text:
        if char in string.ascii_letters:
            string1+=char
        elif char in string.punctuation:
            string2+=char
        else:
            string3+=char
    
    return string1, string2, string3
            



#parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
#print(parts[0])
#print(parts[1])
#print(parts[2])