# Write your solution here

phone_book = {}

while True:
    user_choice = int(input("command (1 search, 2 add, 3 quit):"))
    temp_list = []

    if user_choice == 3:
        print("quitting...")
        break

    if user_choice == 2:
        name = input("name:")
        number = input("number:")
        if name in phone_book:
            temp_list = phone_book[name]
            temp_list.append(number)
            phone_book[name] = temp_list
        else:
           temp_list.append(number)
           phone_book[name] = temp_list

        print("ok!")
    else:
        name = input("name:")
        if name in phone_book:
            for num in phone_book[name]:
                print(num)
        else:
            print("no number")

