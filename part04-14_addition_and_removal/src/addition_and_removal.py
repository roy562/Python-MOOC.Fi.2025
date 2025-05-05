# Write your solution here
my_list = []

while True:
    print("The list is now",my_list)

    user_choice = input("a(d)d, (r)emove or e(x)it:")
    if user_choice == 'x':
        print("Bye!")
        break
    elif user_choice == 'd':
        if len(my_list) == 0:
            my_list.append(1)
        else:
            my_list.append(my_list[-1]+1)
    elif user_choice == 'r':
        my_list.pop(len(my_list)-1)

  #  print("The list is now",my_list)

