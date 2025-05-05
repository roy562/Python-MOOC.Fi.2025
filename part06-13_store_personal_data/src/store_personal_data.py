# Write your solution here

def store_personal_data(person: tuple):
    op_file = 'people.csv'
    with open(op_file,'a') as file:
        write_string = f"{person[0]};{person[1]};{person[2]}\n"
        file.write(write_string)

#personal_data = ("Paul Paulson", 37, 175.5)
#store_personal_data(personal_data)