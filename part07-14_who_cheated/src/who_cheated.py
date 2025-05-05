# Write your solution here
import csv 
from datetime import timedelta

def compare_times(start:str, end:str):
    start_stamps = start.split(":")
    end_stamps = end.split(":")
    start_time = timedelta(hours=float(start_stamps[0]), minutes=float(start_stamps[1]))
    end_time = timedelta(hours=float(end_stamps[0]), minutes=float(end_stamps[1]))
    if (end_time-start_time) > timedelta(hours=float(3)):
        return True

    return False

def cheaters():
    results = []
    start_times = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_times[line[0]] = line[1]

    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file,delimiter=";"):
            if compare_times(start_times[line[0]], line[3]) and line[0] not in results:
                    results.append(line[0])

    return results


#print(cheaters())