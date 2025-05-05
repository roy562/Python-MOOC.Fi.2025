# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word):
    reversed_word = ""

    for i in range(1,len(word)+1):
        #print(word[-1*i])
        reversed_word+=word[-1*i]
    
    #print(reversed_word)
    return word == reversed_word


while True:
    word = input("Please type in a palindrome:")

    if palindromes(word):
        print(word, "is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")