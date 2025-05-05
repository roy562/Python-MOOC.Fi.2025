# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    person1_avg = (person1["result1"]+person1["result2"]+person1["result3"])/3
    person2_avg = (person2["result1"]+person2["result2"]+person2["result3"])/3
    person3_avg = (person3["result1"]+person3["result2"]+person3["result3"])/3
    lowest_average = min(person1_avg, person2_avg, person3_avg)

    if lowest_average == person1_avg:
        return person1
    elif lowest_average == person2_avg:
        return person2
    else:
        return person3


def main():
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
    
#main()