# Write your solution here
def read_input_file(filename):
    file_words = []

    with open(filename) as file:
        for word in file:
            file_words.append(word.strip().lower())

    return file_words

def search_with_period(file_words:list, search_term:str):
    found_words = []

    for word in file_words:
        if len(search_term) != len(word):
            continue
        match_found = True
        for i in range(0,len(search_term)):
            if search_term[i] !="." and word[i]!= search_term[i]:
                match_found = False
        if match_found:
            found_words.append(word)

    return found_words

def search_with_asterisk(file_words:list, search_term:str):
    found_words = []
    for word in file_words:
        if search_term[0] == "*":
            match_found = word.endswith(search_term[1:])
        if search_term[-1] == "*":
            match_found = word.startswith(search_term[:-1])

        if match_found:
            found_words.append(word)

    return found_words

def find_words(search_term: str):
    found_words = []

    file_words = read_input_file("words.txt")
    
    if search_term.find(".") != -1:
        found_words = search_with_period(file_words, search_term)
    elif search_term.find("*") != -1:
        found_words = search_with_asterisk(file_words, search_term)
    else:
        if search_term in file_words:
            found_words.append(search_term)

    return found_words