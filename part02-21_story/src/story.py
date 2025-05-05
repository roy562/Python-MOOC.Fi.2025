# Write your solution here
story =""
last_word = ""

while True:
    word = input("Please type in a word:")
    
    if word == 'end' or last_word == word:
        break

    last_word = word

    story+= word+" "

    

print(story)