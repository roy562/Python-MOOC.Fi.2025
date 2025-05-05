# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0
    @classmethod
    def get_next_id(cls):
        Task.id+=1
        return Task.id

    def __init__(self, description:str, programmer:str, workload:int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.get_next_id()
        self.status = 'NOT FINISHED'
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"

    def is_finished(self):
        return True if self.status == 'FINISHED' else False

    def mark_finished(self):
        self.status = 'FINISHED'

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description:str, programmer:str, workload:int):
        order_task = Task(description, programmer, workload)
        self.__tasks.append(order_task)

    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(set([task.programmer for task in self.__tasks]))

    def mark_finished(self, id: int):
        task_found = False
        for task in self.__tasks:
            if task.id == id:
               task.mark_finished()
               task_found = True

        if not task_found:
            raise ValueError("No matching tasks found")
    
    def finished_orders(self):
        return [task for task in self.__tasks if task.status == 'FINISHED']
    
    def unfinished_orders(self):
        return [task for task in self.__tasks if task.status == 'NOT FINISHED']
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("No matching programmer found")

        finished_tasks = [t for t in self.finished_orders() if t.programmer == programmer]
        unfinished_tasks = [t for t in self.unfinished_orders() if t.programmer == programmer]
        #print(finished_tasks)
        #print(unfinished_tasks)
        finished_workload = sum([task.workload for task in finished_tasks])
        unfinished_workload = sum([task.workload for task in unfinished_tasks])

        return len(finished_tasks), len(unfinished_tasks), finished_workload, unfinished_workload
    

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def __initial_prompt(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def __add_order(self):
        description = input("description: ")
        pro_workload = input("programmer and workload estimate: ").split(" ")
        if len(pro_workload) !=2 or pro_workload[0] == "" or pro_workload[1] == "":
            raise ValueError("Incorrect input")
        programmer = pro_workload[0]
        try:
            workload = int(pro_workload[1])
        except:
            raise ValueError("Incorrect workload input")
        
        self.__orderbook.add_order(description, programmer, workload)
        print('added!')
    
    def __list_finished_tasks(self):
        finished_tasks = self.__orderbook.finished_orders()
        if len(finished_tasks) == 0:
            print("no finished tasks")
        
        for task in finished_tasks:
            print(task)
    
    def __list_unfinished_tasks(self):
        unfinished_tasks = self.__orderbook.unfinished_orders()
        if len(unfinished_tasks) == 0:
            print("no finished tasks")
        
        for task in unfinished_tasks:
            print(task)

    def __mark_finished(self):
        try:
            id = int(input('id: '))
        except:
            raise ValueError()   
        self.__orderbook.mark_finished(id)
        print("marked as finished")
    
    def __list_programmers(self):
        programmers = self.__orderbook.programmers()
        for p in programmers:
            print(p)
    
    def __programmer_status(self):
        programmer = input("programmer: ")
        status = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")


    def execute(self):
        self.__initial_prompt()
        while True:
            print()
            try:
                option = int(input("command: "))
            
                if option == 0:
                    break
                elif option == 1:
                        self.__add_order()
                elif option == 2:
                    self.__list_finished_tasks()
                elif option == 3:
                    self.__list_unfinished_tasks()
                elif option == 4:
                    self.__mark_finished()
                elif option == 5:
                    self.__list_programmers()
                elif option == 6:
                    self.__programmer_status()
                else:
                    raise ValueError("Incorrect input")
            except:
                print("erroneous input")
                continue



app = OrderBookApplication()
app.execute()