import os
import datetime
import markdown
from typing import List
from tag_manager import TagManager
from task import Task


class Storage:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        self.tag_manager = TagManager()
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def get_task_path(self, task_id: int) -> str:
        return os.path.join(self.dir_path, f'{task_id}.md')

    def read_tasks(self) -> List[Task]:
        tasks = []
        for file_name in os.listdir(self.dir_path):
            with open(os.path.join(self.dir_path, file_name), 'r') as file:
                task = self.parse_markdown(file.read())
                task.tags = self.tag_manager.print_tags(
                    self.get_task_path(task.id)).split(',')
                tasks.append(task)
        return tasks

    def write_tasks(self, tasks: List[Task]):
        for task in tasks:
            task_path = self.get_task_path(task.id)
            with open(task_path, 'w') as file:
                # read existing tags so the update can remove+add
                prior_tags = self.tag_manager.print_tags(task_path)
                file.write(self.format_markdown(task))
                self.tag_manager.update_tags(
                    task_path, prior_tags, ','.join(task.tags))

    def delete_task(self, task_id: int):
        os.remove(self.get_task_path(task_id))

    def format_markdown(self, task: Task) -> str:
        # Note: doesn't handle tags (they aren't in the markdown)
        return f'| id | name | due_date | duration | priority | is_recurring |\n| --- | --- | --- | --- | --- | --- |\n| {task.id} | {task.name} | {task.due_date} | {task.duration} | {task.priority} | {task.is_recurring} |'

    def parse_markdown(self, markdown: str) -> Task:
        # Note: doesn't handle tags (they aren't in the markdown)
        lines = markdown.split('\n')
        values = lines[2].split('|')
        try:
            due_date = datetime.datetime.strptime(values[3].strip(), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            due_date = datetime.datetime.strptime(values[3].strip(), "%Y-%m-%d")
        return Task(int(values[1].strip()), values[2].strip(), due_date, int(values[4].strip()), int(values[5].strip()), values[6].strip() == 'True', values[7].strip().split(',') if len(values) > 7 else [])
