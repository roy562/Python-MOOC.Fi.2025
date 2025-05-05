# Write your solution here
filename = 'diary.txt'
print("1 - add an entry, 2 - read entries, 0 - quit")

while True:
    user_choice = int(input("Function:"))
    if user_choice == 0:
        print("Bye now!")
        break
    if user_choice == 1:
        diary_entry = input("Diary entry:")
        with open(filename,'a') as write_file:
            write_file.write(f"{diary_entry}\n")
        print('Diary saved')
    if user_choice == 2:
        print("Entries:")
        with open(filename,'r') as read_file:
            for line in read_file:
                print(line.strip())
