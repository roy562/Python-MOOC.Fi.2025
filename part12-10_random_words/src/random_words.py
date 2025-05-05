# Write your solution here:
from random import sample, shuffle

def word_generator(characters: str, length: int, amount: int):
    wordgen = ("".join(sample(characters,length)) for i in range(amount) )
    return wordgen

def test():
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)

#test()