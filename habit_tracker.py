from datetime import date
import csv
import os
import sys

habits_list = []
to_do_list = []
days_map = {0: "M", 1: "T", 2: "W", 3: "Th", 4: "F", 5: "S", 6: "Su"}
today = days_map[date.today().weekday()]
is_running = True


class Task:
    def __init__(self, name, days=None):
        """A task with a name, days to be completed, 
        frequency to complete, and time_frame for completion"""
        self.name = name
        self.days = days

    def __str__(self):
        if self.days == None:
            return f"{self.name}"
        else:
            str_days = ",".join(self.days) if len(self.days) != 7 else "daily"
            return f"{self.name}; {str_days}"


def read_file():
    with open(os.path.join(sys.path[0], "habits.csv"), "r") as csv_habits:
        reader = csv.reader(csv_habits)
        for line in reader:
            if line[1] == "":
                to_do_list.append(Task(line[0]))
            else:
                habits_list.append(Task(line[0], line[1].split("-")))


def tasks_for_today():
    [print(task.name) for task in habits_list if today in task.days]


def tasks_for_day():
    day = input("Enter M, T, W, Th, F, S, or Su: ")
    [print(task.name) for task in habits_list if day in task.days]


def view_all_habits():
    [print(str(habit)) for habit in habits_list]


def add_task():
    # TODO - Add to CSV
    name = input("Enter the name of the task: ")
    habit_or_todo = input("Is this task a habit or a to-do item: ").lower()
    if habit_or_todo == "habit":
        days = input(
            "Enter days to complete this task (M, T, W, Th, F, S, Su), separated by dashes: "
        )
        habits_list.append(Task(name, days.split("-")))
    else:
        to_do_list.append(Task(name))
    print("Task added!")


def delete_task():
    # TODO - Delete from CSV
    task_removed = False
    task_name = input("Enter the name of the task: ")
    habit_or_todo = input("Is this task a habit or a to-do item: ").lower()
    task_dic = {"to-do item": to_do_list, "to-do": to_do_list, "habit": habits_list}
    for task in task_dic[habit_or_todo]:
        if task.name == task_name:
            task_dic[habit_or_todo].remove(task)
            task_removed = True
            break
    to_print = "Task removed!" if task_removed else "No task found"
    print(to_print)


def view_todo():
    print([str(todo) for todo in to_do_list])


def view_all():
    print("Habits: ")
    view_all_habits()
    print("To-Do: ")
    view_todo()


def close():
    global is_running
    is_running = False


def main():
    read_file()
    operations = {
        "1": tasks_for_today,
        "2": tasks_for_day,
        "3": view_all_habits,
        "4": add_task,
        "5": delete_task,
        "6": view_todo,
        "7": view_all,
        "8": close,
    }
    while is_running:
        i = input(
            """What would you like to do?
        1. View habits for Today
        2. View habits for day
        3. View all habits
        4. Add a task/habit
        5. Delete a task/habit
        6. View to-do list
        7. View all tasks and habits
        8. Close
        Only enter the number: """
        )
        try:
            operations[i]()
        except:
            print("operation not supported")


if __name__ == "__main__":
    main()
