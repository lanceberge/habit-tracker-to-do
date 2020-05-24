from datetime import date
import csv
import os
import sys

task_list = []
to_do_list = []
days_map = {0: 'M', 1: 'T', 2: 'W', 3: 'Th', 4: 'F', 5: 'S', 6: 'Su'}
today = days_map[date.today().weekday()]
tasks_changed = False
is_running = True

class Task:

    def __init__(self, name, days=None):
        """A task with a name, days to be completed, 
        frequency to complete, and time_frame for completion"""
        self.name = name
        self.days = days


    def __str__(self):
        if self.days == None:
            return self.name
        str_days = ','.join([day for day in self.days])
        return f"{self.name}, {str_days}"


def read_list():
    """parses the habits.csv file and adds each list to task_list"""
    tasks_changed = False
    with open(os.path.join(sys.path[0], "habits.csv"), "r") as csv_habits:
        reader = csv.reader(csv_habits)
        for line in reader:
            if line[2] == "":
                to_do_list.append(Task(line[0]))
            else:
                days_list = list(map(int, line[1].split('-')))
                """splits the stores days value into a list, maps it to the int function,
                and converts it to a list"""
                task_list.append(Task(line[0], days_list))


def tasks_for_day(day=today):
    """returns a list of the string output of each task
    for parameter day"""
    return [str(task) for task in task_list if day in task.days]


def add_task(task):
    # TODO - Add task to csv
    task_list.append(task)
    tasks_changed = True

def remove_task(task):
    task_list.remove(task)
    tasks_changed = True

def task_for_today():
    print (tasks_for_day())

def task_for_input_day():
    day = input(
    """Enter the day you would like to view tasks for:
    M, T, W, Th, F, S, or Su
    """)
    print (tasks_for_day(day))

def add_task():
    pass

def delete_task():
    pass

def view_all_tasks():
    print()

def to_do():
    print ([str(task) for task in to_do_list])

def close():
    is_running = False

def main():
    operations = {
        1: task_for_today,
        2: task_for_input_day,
        3: add_task,
        4: delete_task,
        5: view_all_tasks,
        6: to_do,
        7: close 
    }
    while is_running:
        i = input(
        """What would you like to do?
        1. View habits for Today
        2. View habits for day
        3. Add a task/habit
        4. Delete a task/habit
        5. View to-do list
        6. Close
        Only enter the number: """
        )
        operations[i]()


if __name__ == "__main__":
    main()
