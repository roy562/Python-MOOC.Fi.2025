# wwite your solution here

if True:
    students1 = input("Student information:")
    exercises1 = input("Exercises completed:")
    exam_points1 = input("Exam points:")
else:
    students1 = 'students1.csv'
    exercises1 = 'exercises1.csv'
    exam_points1 = 'exam_points1.csv'

students_info = {}
with open(students1) as file:
    for line in file:
        items = line.split(";")
        if items[0] == 'id':
            continue
        students_info[items[0]] = items[1]+" "+items[2].strip()
#print(students_info)

exercises_total = {}
with open(exercises1) as file:
    for line in file:
        items = line.split(";")
        if items[0] == 'id':
            continue
        ex_sum = 0
        for ex in items[1:]:
            ex_sum+=int(ex.strip())
        exercises_total[items[0]] = ex_sum
#print(exercises_total)

exam_total = {}
with open(exam_points1) as file:
    for line in file:
        items = line.split(";")
        if items[0] == 'id':
            continue
        exam_pts_sum = 0
        for pts in items[1:]:
            exam_pts_sum+=int(pts.strip())
        exam_total[items[0]] = exam_pts_sum
#print(exam_total)

def calculate_grade(exercises:int, exam_points:int):
    grade = 0
    exercise_pts = exercises//4
    total_pts = exercise_pts + exam_points

    if total_pts >14 and total_pts <=17:
        grade=1
    elif total_pts >17 and total_pts <=20:
        grade=2
    elif total_pts >20 and total_pts <=23:
        grade=3
    elif total_pts >23 and total_pts <=27:
        grade=4
    elif total_pts > 27:
        grade=5 

    return grade, exercise_pts, total_pts

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for id, name in students_info.items():
    grade, exercise_pts, total_pts = calculate_grade(exercises_total[id], exam_total[id])
    print(f"{name:30}{exercises_total[id]:<10}{exercise_pts:<10}{exam_total[id]:<10}{total_pts:<10}{grade:<10}")