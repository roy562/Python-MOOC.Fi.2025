# Write your solution here
import urllib.request
import json
import math

def retrieve_course(course_name: str):
    course_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course_details = json.loads(course_request.read())

    course_stats = {}
    course_stats['weeks'] = len(course_details)
    
    max_students = 0
    hours = 0
    exercises = 0
    
    for value in course_details.values():
        #print(value)
        max_students = max(value['students'], max_students)
        hours+=value['hour_total']
        exercises+=value['exercise_total']

    hours_average = math.floor(hours/max_students)
    exercises_average = math.floor(exercises/max_students)

    course_stats['students'] = max_students
    course_stats['hours'] = hours
    course_stats['hours_average'] = hours_average
    course_stats['exercises'] = exercises
    course_stats['exercises_average'] = exercises_average

    return course_stats
   

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    all_courses = json.loads(my_request.read())

    active_courses = []

    for course in all_courses:
        if course['enabled'] == False:
            continue
        active_course = (course['fullName'],course['name'],course['year'], sum(course['exercises']))
        #course_detail = retrieve_course(course['name'])
        active_courses.append(active_course)

    #print(active_courses)
    return active_courses




#retrieve_all()
#print(retrieve_course("docker2019"))
