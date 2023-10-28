from typing import List
from task import Task
from storage import Storage


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.read_tasks()

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.storage.write_tasks(self.tasks)

    def update_task(self, task: Task):
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                self.storage.write_tasks(self.tasks)
                return
        raise ValueError("Task not found")

    def delete_task(self, task_id: int):
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                self.storage.delete_task(task_id)
                return
        raise ValueError("Task not found")

    def get_top_priority_tasks(self, count: int) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.priority, reverse=True)[:count]

    def add_tag(self, task_id: int, tag: str):
        for task in self.tasks:
            if task.id == task_id:
                task.tags.append(tag)
        self.storage.write_tasks(self.tasks)

    def remove_tag(self, task_id: int, tag: str):
        for task in self.tasks:
            if task.id == task_id and tag in task.tags:
                task.tags.remove(tag)
        self.storage.write_tasks(self.tasks)

    def update_tag(self, task_id: int, old_tag: str, new_tag: str):
        for task in self.tasks:
            if task.id == task_id and old_tag in task.tags:
                task.tags[task.tags.index(old_tag)] = new_tag
        self.storage.write_tasks(self.tasks)
