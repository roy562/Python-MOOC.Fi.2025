# Write your solution here
def user_input():
    new_list = []
    while True:
        scores = input("Exam points and exercises completed:")

        if scores == "":
            break
        else:
            new_list.append(scores)
    return new_list

def grade(total_score):
        if total_score <=14:
            return 0
        elif total_score >14 and total_score <=17:
            return 1
        elif total_score >=17 and total_score <=20:
            return 2
        elif total_score >20 and total_score <=23:
            return 3
        elif total_score >23 and total_score <=27:
            return 4
        else:
            return 5

def statistics(total_points:list, grades:list):
    print("Statistics:")
    pts_average = sum(total_points)/len(total_points)
    print(f"Points average: {pts_average:.1f}")

    pass_percentage = ((len(grades)-grades.count(0))/len(grades))*100
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    grade_dist = ""
    print("Grade distribution:")
    for i in range(5,-1,-1):
        #grade_dist = "*" * grades.count(i)
        print(f"  {i}: {"*" * grades.count(i)}")

def aggregate(exam_scores:list):
    total_pts = []
    grades = []
    scores = []
    total_score = 0
    for item in exam_scores:
        scores = item.split(" ")
        total_score = int(scores[0]) + int(scores[1])//10
        
        total_pts.append(total_score)
        
        if int(scores[0]) < 10:
            grades.append(0)
        else:
            grades.append(grade(total_score))
#    print(total_pts)
#    print(grades)
    statistics(total_pts, grades)
    return



def main():
    exam_scores = user_input()
#    print(exam_scores)
    aggregate(exam_scores)

main()