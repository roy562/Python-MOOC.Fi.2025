# Write your solution here
sentence = input("Please type in a sentence:")

i=0

while i < len(sentence):
    if i == 0:
        print(sentence[i])

    if sentence[i] == " ":
        print(sentence[i+1])

    i+=1