def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]

        if not validate_name(name):
            print(f"Error: missing name")
            continue
        if not validate_grades(grades):
            print(f"Error: {name} has no grades")
            continue

        student_stats = calculat_student_stats(grades)

        result_names.append(name)
        result_averages.append(round(student_stats["average"], 1))
        result_statuses.append(student_stats["status"])
        result_highs.append(student_stats["highest"])
        result_lows.append(student_stats["lowest"])
    
    print_repo(result_names, result_averages, result_statuses, result_lows, result_highs)
    
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
    return result_names, result_averages, result_statuses

def validate_name(name):
    return bool(name)

def validate_grades(grades):
    return bool(grades)

def calculat_student_stats(grades):
    return {"total": sum(grades), "average": sum(grades)/len(grades), "status": "pass" if \
            (sum(grades)/len(grades)) >= 56 else "fail", "highest": max(grades), "lowest": min(grades)}

def print_repo(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"""
    Name: {result_names[i]}
        Average: {result_averages[i]}
        Status: {result_statuses[i]}
        Range: {result_lows[i]} - {result_highs[i]}\n""")