# Write your solution here
from random import choice

def read_input_file(ip_file):
    words_list = []
    with open(ip_file) as file:
        for word in file:
            words_list.append(word.strip())
    return words_list


def words(n: int, beginning: str):
    file_words = read_input_file("words.txt")
    results = []

    words_starting_with_str = [i for i in file_words if i.startswith(beginning)]

    if len(words_starting_with_str) < n:
            raise ValueError("Not enough words left to choose from")

    for i in range(0,n):
        if len(words_starting_with_str) == 0:
            raise ValueError("Not enough words left to choose from")
        else:
            random_word = choice(words_starting_with_str)
            if random_word in results:
                words_starting_with_str.remove(random_word)
                continue
            else:
                results.append(random_word)
    return results

def main():
    word_list = words(3, "ca")
    for word in word_list:
        print(word)

#main()