import csv
import re
# "./reader/chris/output2.csv"

class Course():
    
    def __init__(self, course_name, start_time, end_time,):
        
        self.course_name=course_name
        self.start_time= start_time
        self.end_time= end_time
    
    def __str__(self):
        return self.course_name
    

def schedule_maker(csv_file): 
    file = open(csv_file, "r")
    data = list(csv.reader(file, delimiter= ","))
    file.close()

    course_list=[]
    time_list=[]
    new_time_list=[]
    day_list=[]
    start_time=[]
    end_time=[]


    days_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for sub_list in data:

        for i in range(len(sub_list)):
            if sub_list[i][0:3].isupper():
                course_list.append(sub_list[i])
                day_list.append(days[i-1])
            if "-" in sub_list[i] and ("am" in sub_list[i] or "pm" in sub_list[i]):
                time_list.append(sub_list[i])
            if re.match(r"[0-9]+:\d\d.[a-zA-Z]+-[0-9]+:\d\d.[a-zA-Z]+", sub_list[i]):
                new_time_list.append(re.findall(r"([0-9]+:\d\d.[a-zA-Z]+-[0-9]+:\d\d.[a-zA-Z]+)", sub_list[i]))
                
    # print("day", day_list, len(day_list))
    for time in new_time_list:
        sub_time=time[0].split("-") 
        start_time.append(sub_time[0])
        end_time.append(sub_time[1])

    for i in range(len(course_list)):
        days_dict[day_list[i]] += [Course(course_list[i], start_time[i], end_time[i])]

    return days_dict

    # print("course", course_list, len(course_list))
    # print("new time", new_time_list, len(new_time_list))
    # print("starts", start_time, len(start_time))
    # print("end", end_time, len(end_time))
    # print(" ------------------------------------------------------------")
    # print(days_dict)

if __name__ == '__main__':
    print(schedule_maker('output3.csv'))