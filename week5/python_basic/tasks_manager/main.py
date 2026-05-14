class Task:
    def __init__(self, task_name, priority_level):
        self.name = task_name
        self.priority_level = priority_level
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True

    def mark_incomplete(self):
        self.is_complete = False

    def change_priority_level(self, new_priority_level):
        self.priority_level = new_priority_level

    def __str__(self):
        return f"""
Task name: {self.name}
Priority level: {"High" if self.priority_level == 3 else "Medium" if self.priority_level == 2 else "Low"}
Status: {"Completed" if self.is_complete else "Not completed"}\n\n
"""
        
        
def print_task_stats(task_name, tasks):
    for task in tasks:
        if task.name == task_name:
            return task
    return f"Task {task_name} not found..."

def mark_as_completed(task_name, tasks):
    for task in tasks:
        if task.name == task_name:
            task.mark_complete()
            return f"Task: {task_name} marked as complete\nGreat job!"
    return f"Task {task_name} not found..."

def mark_as_incomplete(task_name, tasks):
    for task in tasks:
        if task.name == task_name:
            task.mark_incomplete()
            return f"Task: {task_name} marked as incomplete\nHurry up..."
    return f"Task {task_name} not found..."  

def incompleted_tesks(tasks):
    return [task for task in tasks if not task.is_complete] 

def completed_tasks(tasks):
    return [task for task in tasks if task.is_complete]

def identify_urgent_tasks(tasks):
    return [task for task in tasks if task.priority_level == 3]

def delete_task(task_name, tasks):
    for task in tasks:
        if task.name == task_name:
            return task
    return False

def get_daily_summary(tasks):
    number_of_incomplete = len(incompleted_tesks(tasks))
    number_of_completed = len(completed_tasks(tasks))
    number_of_urgent_tasks = len(identify_urgent_tasks(tasks))
    return [number_of_incomplete, number_of_completed, number_of_urgent_tasks]

def menu():
    return"""
    ========= TASKS MANAGER =========

    1. Add a task to the task list
    2. See task's status
    3. Mark a task as complete
    4. Mark a task as incomplete
    5. See completed tasks
    6. See incompleted tasks
    7. Identify urgent tasks
    8. Show daily summary
    9. Delete task
"""

def main():
    tasks = []
    print("=======================================================")
    print("============= WELCOME TO OUT TASK MANAGER =============")
    print("=======================================================\n")
    while True:
        print(tasks)
        print(menu())
        user_choice = input("Enter your choice [or quit to exit]: ")
        
        if user_choice == "quit":
            print("Bye bye\nSee you next time...")
            exit()
        
        if user_choice == "1":
            task_name = input("Enter your task name: ")
            priority_level = int(input("Enter the priority task's level [1-3]: "))
            tasks.append(Task(task_name, priority_level))
            print(f"Task {task_name} added successully to your tasks list!")
        
        elif user_choice == "2":
            task_name = input("Enter a task name are you looking for: ")
            print("=================================")
            print(print_task_stats(task_name, tasks))
            print("=================================")
        
        elif user_choice == "3":
            task_name = input("Which task did you complete? ")
            print(mark_as_completed(task_name, tasks))
        
        elif user_choice == "4":
            task_name = input("Which task do you want to mark as incomplete? ")
            print(mark_as_incomplete(task_name, tasks))
        
        elif user_choice == "5":
            all_completed = completed_tasks(tasks)
            if not all_completed:
                print("No completed tasks")
                continue
            print("All completed tasks:")
            for task in all_completed:
                print(task, end="|")
        
        elif user_choice == "6":
            all_incomplete = incompleted_tesks(tasks)
            if not all_incomplete:
                print("No incomplete tasks")
                continue
            print("All incomplete tasks:")
            for task in all_incomplete:
                print(task, end="|")
            print("\nHurry up to compelte them!")
        
        elif user_choice == "7":
            urgent_tasks = identify_urgent_tasks(tasks)
            print("All urgent tasks:")
            if not urgent_tasks:
                print("No urgent tasks")
                continue
            for task in urgent_tasks:
                print(task, end="|")
            print("\nIn case you didn't complete them, you know what to do...")
        
        elif user_choice == "8":
            daily_summary = get_daily_summary(tasks)
            print(f"""
    ================ DAILY SUMMARY ================
    
    There are {len(tasks)} tasks in the system
    {daily_summary[0]} tasks are still incomplete
    {daily_summary[1]} tasks are completed
    {daily_summary[2]} tasks are marked as identify urgent

    ================ FINISH SUMMARY ===============
    """)

        elif user_choice == "9":
            task_name = input("Enter the task name do you want to delete: ")
            task = delete_task(task_name, tasks)
            if not task:
                print(f"Task {task_name} not found...")
            else:
                tasks.remove(task)
                print(f"Task {task_name} was deleted successfully.")


if __name__ == "__main__":
    main()