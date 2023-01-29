import text
import textract_table
from models import User, Day, Course

schedule_dict = text.schedule_maker('output3.csv')

user = User("Placeholder")
user.save()

for current_day in dict.keys(schedule_dict):
    day_of_the_week = user.day_set.create(day = current_day)

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

        
        
        print(current_course.current_course_name, current_course.start_time, current_course.end_time)


        day_of_the_week.course_set.create(course = current_course, start_time = current_course.start_time, end_time = current_course.end_time)


