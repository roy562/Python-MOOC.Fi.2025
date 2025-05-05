# Write your solution here
from difflib import get_close_matches

valid_words = []
invalid_words = []
with open("wordlist.txt") as words_file:
    for word in words_file:
        valid_words.append(word.strip())

user_text = input("write text:")
user_text_parts = user_text.split(" ")

for word in user_text_parts:
    if word.lower() in valid_words:
        print(word, end=" ")
    else:
        print(f"*{word}*", end=" ")
        invalid_words.append(word)
print()
print("suggestions:")
for word in invalid_words:
    suggestions = get_close_matches(word, valid_words)
    print(f"{word}: {", ".join(suggestions)}")