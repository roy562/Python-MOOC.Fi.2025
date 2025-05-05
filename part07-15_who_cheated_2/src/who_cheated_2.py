# Write your solution here
import csv 
from datetime import datetime, timedelta

def final_points():
    results = {}
    start_times = {}
    submissions = {}
    with open("start_times.csv") as start_file, open("submissions.csv") as sub_file:
        for student in csv.reader(start_file, delimiter=";"):
            name = student[0]
            start_time = datetime.strptime(student[1],'%H:%M')
            start_times[name] = start_time
    
        for submission in csv.reader(sub_file, delimiter=";"):
            name = submission[0]
            task = submission[1]
            points = int(submission[2])
            submission_time = datetime.strptime(submission[3],'%H:%M')
            if submission_time - start_times[name] > timedelta(hours=3):
                continue
            else:
                key = name+";"+task
                if key in submissions:
                    submissions[key] = max(submissions[key], points)
                else:
                    submissions[key] = points
    print(submissions)
    for key,value in submissions.items():
        name_task = key.split(";")
        name = name_task[0]
        if name in results:
            results[name]+=value
        else:
            results[name]=value

    return results


#print(final_points())