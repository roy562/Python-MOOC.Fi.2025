# write your solution here
def read_fruits():
    new_dict = {}
    with open("fruits.csv") as my_file:
        for line in my_file:
            line = line.replace("\n","")
            
            words = line.split(";")
            #print(words)
            new_dict[words[0]] = float(words[1])
    return new_dict

#print(read_fruits())