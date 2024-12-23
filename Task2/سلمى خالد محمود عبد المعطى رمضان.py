def schedule_exams(courses, students):

    conflicts = {course: set() for course in courses}

    for course1 in courses:
        for course2 in courses:
            if course1 != course2:
                
                if set(students[course1]) & set(students[course2]):
                    conflicts[course1].add(course2)

    
    sorted_courses = sorted(conflicts.keys(), key=lambda x: len(conflicts[x]), reverse=True)

    
    time_slots = {}
    for course in sorted_courses:
        
        used_slots = {time_slots[neighbor] for neighbor in conflicts[course] if neighbor in time_slots}
        
        for slot in range(len(courses)):
            if slot not in used_slots:
                time_slots[course] = slot
                break

    return time_slots

courses = ["Software", "Algorithm", "Big data", "Mobile app", "Computer"]
students = {
    "Software": ["Alice", "Bob", "Charlie"],
    "Algorithm": ["Alice", "Charlie"],
    "Big data": ["Bob", "Charlie"],
    "Mobile app": ["Alice", "David"],
    "Computer": ["David", "Charlie"],
}

exam_schedule = schedule_exams(courses, students)


print("exam schedule")
for course, slot in sorted(exam_schedule.items(), key=lambda x: x[1]):
    print(f"material: {course}, : time period {slot}")