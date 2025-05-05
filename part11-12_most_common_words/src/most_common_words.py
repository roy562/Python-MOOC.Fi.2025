# WRITE YOUR SOLUTION HERE:
from string import ascii_letters

def most_common_words(filename: str, lower_limit: int):
    all_words = []
    with open(filename) as file:
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                word = "".join([char for char in word if char in ascii_letters])
                all_words.append(word)
            #print(all_words)
    
    return {word: all_words.count(word) for word in all_words if all_words.count(word) >= lower_limit}

#print(most_common_words("comprehensions.txt", 3))
