# Write your solution here
from string import digits, ascii_uppercase
import operator

def find_locations(program:list):
    locations = {}
    for i in range(len(program)):
        cmd = program[i]
        if cmd.endswith(":"):
            location_name = cmd[:-1]
            locations[location_name] = i
    #print(locations)
    return locations

def get_opr_value(opr:str, variables:dict):
    if opr in ascii_uppercase:
        if opr in variables:
            return variables[opr]
        else:
            return 0
    else:
        return int(opr)

def exec_math_cmd(cmd_parts:str, variables:dict):
    if len(cmd_parts) !=3:
        return
    
    action = cmd_parts[0]
    opr1 = cmd_parts[1]
    opr2 = cmd_parts[2]
    #print(action, opr1, opr2)

    if action == "MOV":
        variables[opr1] = get_opr_value(opr2,variables)

    if action == "ADD":
        variables[opr1] = get_opr_value(opr1, variables)+get_opr_value(opr2, variables)
        
    if action == "SUB":
        variables[opr1] = get_opr_value(opr1, variables)-get_opr_value(opr2, variables)

    if action == "MUL":
        variables[opr1] = get_opr_value(opr1, variables)*get_opr_value(opr2, variables)

def exec_print_cmd(cmd_parts:str, variables:dict, result:list):
    if cmd_parts[0] == "PRINT":
        opr = get_opr_value(cmd_parts[1], variables)
        result.append(opr)
        #print(result)
    
def execute_if_cmd(cmd_parts, variables):
    ops = {"==":operator.eq, "!=":operator.ne, "<":operator.lt, ">":operator.gt, "<=":operator.le, ">=":operator.ge}
    cond_left_opr = get_opr_value(cmd_parts[1], variables)
    condition = cmd_parts[2]
    cond_right_opr = get_opr_value(cmd_parts[3], variables)
    
    return ops[condition](cond_left_opr, cond_right_opr)

def run(program:list):
    result = []
    variables = {}
    i=0

    locations = find_locations(program)

    while i < len(program):
        #print(f"\nStep {i+1}")
        command = program[i]
        cmd_parts = command.split(" ")
        
        #print(command)
        
        if command == "END":
            return result

        if cmd_parts[0] == "JUMP":
            i = locations[cmd_parts[1]]
            continue

        exec_math_cmd(cmd_parts, variables)
        exec_print_cmd(cmd_parts, variables, result)
        
        if cmd_parts[0] == "IF":
           condition = execute_if_cmd(cmd_parts, variables)
           if condition == True:
                i = locations[cmd_parts[-1]]

        i=i+1
    #print(variables)
    return result

def main1():
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

def main0():
    program0 = []
    program0.append("PRINT A")
    program0.append("END")
    result = run(program0)
    print(result)

def main2():
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

def main3():
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

def main4():
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)

def main5():
    program5 = []
    program5.append("MOV A 1")
    program5.append("MOV B 999")
    program5.append("start:")
    program5.append("ADD A 1")
    program5.append("SUB B 1")
    program5.append("ADD C 1")
    program5.append("IF A == B JUMP end")
    program5.append("JUMP start")
    program5.append("end:")
    program5.append("PRINT C")
    result = run(program5)
    print(result)

#main0()
#main1()
#main2()
#main3()
#main4()
#main5()