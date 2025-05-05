def read_students_file(students1):
    students_info = {}
    with open(students1) as file:
        for line in file:
            items = line.split(";")
            if items[0] == 'id':
                continue
            students_info[items[0]] = items[1]+" "+items[2].strip()
    
    return students_info

def read_exercises_file(exercises1):
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

    return exercises_total

def read_exam_points_file(exam_points1):
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

    return exam_total

def read_course_file(course1):
    file_header = []
    with open(course1) as file:
        for line in file:
            parts = line.split(":")
            file_header.append(parts[1].strip())

    return file_header

def calculate_grade(total_pts:int):

    if total_pts <=14:
        return 0
    elif total_pts <=17:
        return 1
    elif total_pts <=20:
        return 2
    elif total_pts <=23:
        return 3
    elif total_pts <= 27:
        return 4
    else:
        return 5 

def write_statistics_file(op_results_txt, students_info:dict, 
                          exercises:dict, exam_points:dict, course:list):
    header = f"{course[0]}, {course[1]} credits\n"
    header+= "=" * len(header.strip())+"\n"
    header+= f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"

    with open(op_results_txt,'w') as op_file:
        op_file.write(header)
        for id, name in students_info.items():
            data_string = ""

            exec_pts = exercises[id]//4
            exm_pts = exam_points[id]
            tot_pts = exec_pts+exm_pts
            grade = calculate_grade(tot_pts)
            
            data_string = f"{name:30}{exercises[id]:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n"
            op_file.write(data_string)

def write_grades_file(op_results_csv, students_info:dict, exercises:dict, exam_points:dict):
    with open(op_results_csv,'w') as op_file:
        for id, name in students_info.items():
            data_string = ""
            grade = calculate_grade((exercises[id]//4)+exam_points[id])
            data_string = f"{id};{name};{grade}\n"
            op_file.write(data_string)

def main():
    if True:
        students1 = input("Student information:")
        exercises1 = input("Exercises completed:")
        exam_points1 = input("Exam points:")
        course1 = input("Course information:")
    else:
        students1 = 'students1.csv'
        exercises1 = 'exercises1.csv'
        exam_points1 = 'exam_points1.csv'
        course1 = 'course1.txt'

    op_results_txt = 'results.txt'
    op_results_csv = 'results.csv'

    students_info = read_students_file(students1)
    exercises = read_exercises_file(exercises1)
    exam_points = read_exam_points_file(exam_points1)
    course = read_course_file(course1)

    write_statistics_file(op_results_txt, students_info, exercises, exam_points, course)
    write_grades_file(op_results_csv, students_info, exercises, exam_points)
    print(f"Results written to files {op_results_txt} and {op_results_csv}")

main()







