def active_and_over_18(students_list):
    active_students = []
    for student in students_list:
        if student[1] >= 18 and student[2] == "active":
            active_students.append(student[0])
    return active_students

students = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(active_and_over_18(students))
