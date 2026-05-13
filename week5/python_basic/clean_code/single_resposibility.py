def manage_students(names, grades, new_name, new_grade):
    # validation
    if not valid_new_name(new_name):
        print("Error: invalid name")
        return None

    if not valid_new_grade(new_grade):
        print("Error: grade must be 0-100")
        return None

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print_report(names, average, top_count, failing_count, grades)

    # save to file
    save_to_file(names, grades)

    return names, grades


def valid_new_name(new_name):
    return bool(new_name) and len(new_name) >= 2


def valid_new_grade(new_grade):
    return 0 <= new_grade <= 100


def print_report(names, average, top_count, failing_count, grades):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")


def save_to_file(names, grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")