import text
import textract_table

schedule_dict = text.schedule_maker('output3.csv')

for day in dict.keys(schedule_dict):
    for course in schedule_dict[day]:
        
        if "pm" in course.start_time:
            time = course.end_time.split(":")
            time[1] = time[1][:2]
            time[0] = time[0].strip()
            time[0] = str(int(time[0]) + 12)

            if time[0] == "24":
                time[0] = "12"
            course.start_time = ":".join(time)
        else:
            course.start_time = course.start_time[:-2].strip()
        
        if "pm" in course.end_time:
            time = course.end_time.split(":")
            time[1] = time[1][:2]
            time[0] = time[0].strip()
            time[0] = str(int(time[0]) + 12)

            if time[0] == "24":
                time[0] = "12"
            course.end_time = ":".join(time)
        else:
            course.end_time = course.end_time[:-2].strip()

        
        
        print(course.course_name, course.start_time, course.end_time)




