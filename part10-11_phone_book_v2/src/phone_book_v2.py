
# Write your solution here:
class Person:
    def __init__(self, name:str):
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        return self.__address
    
    def add_number(self, number:str):
        self.__numbers.append(number)
    
    def add_address(self, address:str):
        self.__address = address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            person = Person(name)
            self.__persons[name] = person

        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            person = Person(name)
            self.__persons[name] = person

        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person == None:
            print("address unknown")
            print("number unknown") 
            return 
        else:
            print("name:", name)
            if len(person.numbers()) == 0 :
                print("number unknown")
            else:
                print(",".join(person.numbers()))

            if person.address() == None:
                print("address unknown")
            else:
                print(person.address())

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

def main1():
    person = Person("Eric")
    print(person.name())
    print(person.numbers())
    print(person.address())
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers())
    print(person.address())

#main1()

def main2():
    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Emily"))

#main2()