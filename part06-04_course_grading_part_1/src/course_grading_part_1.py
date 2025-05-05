# write your solution here
if True:
    student_info1 = input("Student information:")
    exrc_comp1 = input("Exercises completed:")
else:
    student_info1 = 'students1.csv'
    exrc_comp1 = 'exercises1.csv'

st1_info = {}
with open(student_info1) as students1:
    for line in students1:
        line = line.strip()
        #print(line)
        items = line.split(";")
        if items[0] == 'id':
            continue
        st1_info[int(items[0])] = items[1]+" "+items[2]
#print(st1_info)

st1_comp_exers = {}
with open(exrc_comp1) as exercises1:
    for line in exercises1:
        line = line.strip()
        items = line.split(";")
        if items[0] == 'id':
            continue
        st1_comp_exers[int(items[0])] = []
        for exercises in items[1:]:
            st1_comp_exers[int(items[0])].append(int(exercises))
#print(st1_comp_exers)

for student_id, name in st1_info.items():
    total_exercises = sum(st1_comp_exers[student_id])
    print(name, total_exercises)