# Write your solution here
def no_vowels(my_string):
    new_string=my_string
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        print(vowel)
        new_string = new_string.replace(vowel,'')
        print(new_string)

    return new_string