# Write your solution here:
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
        finished_workload = sum([task.workload for task in finished_tasks])
        unfinished_workload = sum([task.workload for task in unfinished_tasks])

        return len(finished_tasks), len(unfinished_tasks), finished_workload, unfinished_workload
    

def test1():
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

#test1()
#print()
def test2():
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

#test2()
#print()

def test3():
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)
    #orders.mark_finished(4)

    for order in orders.all_orders():
        print(order)

#test3()

def test4():
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

test4()