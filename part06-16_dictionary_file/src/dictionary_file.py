# Write your solution here
def add_entry(dict_file):
    finnish_word = input("The word in Finnish:")
    english_word = input("The word in English:")

    with open(dict_file,'a') as file:
        file.write(f"{finnish_word} - {english_word}\n")

    print("Dictionary entry added")

def search_entry(dict_file):
    search_term = input("Search term:")

    with open(dict_file) as file:
        for line in file:
            if line.find(search_term) != -1:
                print(line.strip())

def main():
    
    dictionary_file = 'dictionary.txt'
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function:"))
        
        if function == 3:
            print("Bye!")
            break
        
        if function == 1:
            add_entry(dictionary_file)
        else:
            search_entry(dictionary_file)

main()