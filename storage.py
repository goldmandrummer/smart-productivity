import os
import datetime
import markdown
from typing import List
from task import Task

class Storage:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def read_tasks(self) -> List[Task]:
        tasks = []
        for file_name in os.listdir(self.dir_path):
            with open(os.path.join(self.dir_path, file_name), 'r') as file:
                task = self.parse_markdown(file.read())
                tasks.append(task)
        return tasks

    def write_tasks(self, tasks: List[Task]):
        for task in tasks:
            with open(os.path.join(self.dir_path, f'{task.id}.md'), 'w') as file:
                file.write(self.format_markdown(task))

    def delete_task(self, task_id: int):
        os.remove(os.path.join(self.dir_path, f'{task_id}.md'))

    def format_markdown(self, task: Task) -> str:
        return f'| id | name | due_date | duration | priority | is_recurring |\n| --- | --- | --- | --- | --- | --- |\n| {task.id} | {task.name} | {task.due_date} | {task.duration} | {task.priority} | {task.is_recurring} |'

    def parse_markdown(self, markdown: str) -> Task:
        lines = markdown.split('\n')
        values = lines[2].split(' | ')
        return Task(int(values[1]), values[2], datetime.datetime.strptime(values[3], "%Y-%m-%d"), int(values[4]), int(values[5]), values[6] == 'True')