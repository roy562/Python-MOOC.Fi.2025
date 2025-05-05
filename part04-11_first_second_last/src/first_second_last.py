# Write your solution here
def first_word(sentence):
    first_space_index = sentence.find(" ")
    return sentence[0:first_space_index]

def second_word(sentence):
    first_space_index = sentence.find(" ")
    new_sentence=sentence[first_space_index+1:]
    second_space_index = new_sentence.find(" ")
    if second_space_index==-1:
        return new_sentence
    else:
        return new_sentence[0:second_space_index]

def last_word(sentence):
    index=0
    lastword=""
    while True:
        index=sentence.find(" ")
        if index == -1:
            lastword = sentence
            break
        else:
            sentence = sentence[index+1:]
    return lastword

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))