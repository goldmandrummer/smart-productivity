from task_manager import TaskManager
from task import Task
from storage import Storage
from datetime import datetime

def main():
    storage = Storage('tasks.json')
    task_manager = TaskManager(storage)

    while True:
        top_tasks = task_manager.get_top_priority_tasks(3)
        for task in top_tasks:
            print(task)

        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter task id: "))
            name = input("Enter task name: ")
            due_date = datetime.strptime(input("Enter due date (yyyy-mm-dd): "), "%Y-%m-%d")
            duration = int(input("Enter task duration: "))
            priority = int(input("Enter task priority: "))
            is_recurring = input("Is the task recurring (yes/no): ") == 'yes'
            task = Task(id, name, due_date, duration, priority, is_recurring)
            task_manager.add_task(task)
        elif choice == '2':
            id = int(input("Enter task id: "))
            name = input("Enter task name: ")
            due_date = datetime.strptime(input("Enter due date (yyyy-mm-dd): "), "%Y-%m-%d")
            duration = int(input("Enter task duration: "))
            priority = int(input("Enter task priority: "))
            is_recurring = input("Is the task recurring (yes/no): ") == 'yes'
            task = Task(id, name, due_date, duration, priority, is_recurring)
            task_manager.update_task(task)
        elif choice == '3':
            id = int(input("Enter task id: "))
            task_manager.delete_task(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
