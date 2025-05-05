# write your solution here
if True:
    input_text = input("Write text:")
else:
    input_text = 'We use ptython to make a spell checker'

valid_words = []
with open('wordlist.txt') as file:
    for line in file:
        valid_words.append(line.strip().lower())

#print(len(valid_words))
input_words = input_text.split(" ")
for word in input_words:
    if word.lower() not in valid_words:
        word = f"*{word}*"
    print(word,end=" ")
