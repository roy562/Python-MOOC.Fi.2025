# Write your solution here
phone_book = {}

while True:
    user_choice = int(input("command (1 search, 2 add, 3 quit):"))

    if user_choice == 3:
        print("quitting...")
        break

    if user_choice == 2:
        name = input("name:")
        number = input("number:")
        phone_book[name] = number
        print("ok!")
    else:
        name = input("name:")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")

