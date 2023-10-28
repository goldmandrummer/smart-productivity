import argparse
from task_manager import TaskManager
from task import Task
from storage import Storage
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Task Manager')
    parser.add_argument('--dir', default='tasks', help='Directory to store tasks')
    args = parser.parse_args()

    storage = Storage(args.dir)
    task_manager = TaskManager(storage)

    while True:
        top_tasks = task_manager.get_top_priority_tasks(3)
        for task in top_tasks:
            print(task)

        print('\n')
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter task id: "))
            name = input("Enter task name: ")
            due_date_input = input("Enter due date (yyyy-mm-dd): ")
            time_input = input("Enter time (HH:MM:SS, optional): ")
            if time_input:
                due_date = datetime.strptime(f"{due_date_input} {time_input}", "%Y-%m-%d %H:%M:%S")
            else:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
            duration = int(input("Enter task duration: "))
            priority = int(input("Enter task priority: "))
            is_recurring = input("Is the task recurring (yes/no): ") == 'yes'
            task = Task(id, name, due_date, duration, priority, is_recurring)
            task_manager.add_task(task)
        elif choice == '2':
            id = int(input("Enter task id: "))
            name = input("Enter task name: ")
            due_date_input = input("Enter due date (yyyy-mm-dd): ")
            time_input = input("Enter time (HH:MM:SS, optional): ")
            if time_input:
                due_date = datetime.strptime(f"{due_date_input} {time_input}", "%Y-%m-%d %H:%M:%S")
            else:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
            duration = int(input("Enter task duration: "))
            priority = int(input("Enter task priority: "))
            is_recurring = input("Is the task recurring (yes/no): ") == 'yes'
            task = Task(id, name, due_date, duration, priority, is_recurring)
            task_manager.update_task(task)
        elif choice == '3':
            response = input("Enter task id (or cancel by entering no input): ").strip()
            if not response or len(response) == 0:
                continue
            task_manager.delete_task(int(response))
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
