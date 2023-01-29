
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from schedule_maker import *
import textract_table
from models import User, Day, Course


schedule = schedule_maker('output3.csv')

current_user = "Placeholder"
current_friend = "Place Friend"

def into_database(schedule_dict, friend):
    user = User(current_user)
    user.save()
    user.friend_set.create(name = f"{friend}")
    
    working_friend = user.friend_set.get(name = friend)

    for current_day in dict.keys(schedule_dict):
        day_of_the_week = working_friend.day_set.create(day = current_day)
        day_of_the_week = working_friend.day_set.get(day = current_day)

        for current_course in schedule_dict[current_day]:
            
            if "pm" in current_course.start_time:
                time = current_course.end_time.split(":")
                time[1] = time[1][:2]
                time[0] = time[0].strip()
                time[0] = str(int(time[0]) + 12)

                if time[0] == "24":
                    time[0] = "12"
                current_course.start_time = ":".join(time)
            else:
                current_course.start_time = current_course.start_time[:-2].strip()
            
            if "pm" in current_course.end_time:
                time = current_course.end_time.split(":")
                time[1] = time[1][:2]
                time[0] = time[0].strip()
                time[0] = str(int(time[0]) + 12)

                if time[0] == "24":
                    time[0] = "12"
                current_course.end_time = ":".join(time)
            else:
                current_course.end_time = current_course.end_time[:-2].strip()
        
        day_of_the_week.course_set.create(course = current_course, start_time = current_course.start_time, end_time = current_course.end_time)
    print(current_course.current_course_name, current_course.start_time, current_course.end_time)

if __name__ == 'main':
    into_database(schedule, current_friend)

