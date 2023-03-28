import datetime
import csv
import re


def task_add(taches):
    verif = False

    name_task_add = input(str("Enter the name of the task: "))
    while verif == False :
        dateline_str = input(str("Enter the dateline of the task: (dd/mm/yyyy)"))
        if not re.match(r"^(?:31\/(?:0?[13578]|1[02])|(?:29|30)\/(?:0?[13-9]|1[0-2])|(?:0?[1-9]|1\d|2[0-8])\/(?:0?[1-9]|1[0-2]))\/\d{4}$", dateline_str):
            print("Invalid date, please enter a valid date")
        else :
            verif = True
    

    dateline = datetime.datetime.strptime(dateline_str, "%d/%m/%Y")
    taches.append(
        {"name ": name_task_add, "completed ": False, "dateline ": dateline})
    save_list(taches)
    task_list(taches)
    print("\033[1;36mTask added successfully")


def task_list(taches):
    print("task list :")
    order = input(str("Sort by 1- Index 2- Date \n"))

    if order == '1':
        for i, task in enumerate(taches):
            checkbox = "[X]" if task["completed "] else "[ ]"
            print(f"{i + 1} - {task['name ']} {checkbox} {task['dateline ']}")
    elif order == '2':
        sorted_tasks = sorted(taches, key=lambda x: str(
            x['dateline ']), reverse=True)
        for i, task in enumerate(sorted_tasks):
            checkbox = "[X]" if task["completed "] else "[ ]"
            print(f"{i + 1} - {task['name ']} {checkbox} {task['dateline ']}")
    else:
        print("Invalid order, displaying by index:")
        for i, task in enumerate(taches):
            checkbox = "[X]" if task["completed "] else "[ ]"
            print(f"{i + 1} - {task['name ']} {checkbox} {task['dateline ']}")
    print("End of the task list")


def task_remove(taches):

    task_number = int(input("Enter the number of the task to remove: "))
    if task_number > 0 and task_number <= len(taches):
        del taches[task_number - 1]
        save_list(taches)
        task_list(taches)
        print("Task removed successfully")
    else:
        print("Error")


def task_check(taches):
    name_task_check = int(input("Enter the number of the task to check: "))
    if name_task_check > 0 and name_task_check <= len(taches):
        taches[name_task_check -
               1]["completed "] = not taches[name_task_check - 1]["completed "]
        save_list(taches)
        task_list(taches)
        print("Task checked successfully")
    else:
        print("Error")


def save_list(taches):
    with open("task.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "completed", "dateline"])
        for taches in taches:
            writer.writerow(
                [taches["name "], taches["completed "], taches["dateline "]])


def load_list():
    taches = []
    try:
        with open("task.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                taches.append(
                    {"name ": row[0], "completed ": row[1], "dateline ": row[2]})
    except FileNotFoundError:
        pass
    return taches


def print_statistics(taches):
    total_tasks = len(taches)
    completed_tasks = len([task for task in taches if task["completed "]])
    in_progress_tasks = total_tasks - completed_tasks
    print(f"\033[1;30mTotal tasks: {total_tasks} \n \033[1;31mCompleted tasks: {completed_tasks} \n \033[1;32mIn progress tasks: {in_progress_tasks} \n \033[1;33mPercentage of completed tasks: {completed_tasks / total_tasks * 100:.2f}% \n \033[1;36mPercentage of in progress tasks: {in_progress_tasks / total_tasks * 100:.2f}%")
