import datetime
import json
from typing import List
from task import Task

class Storage:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_tasks(self) -> List[Task]:
        with open(self.file_path, 'r') as file:
            tasks = json.load(file)
            return [Task(**task) for task in tasks]

    def write_tasks(self, tasks: List[Task]):
        with open(self.file_path, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file, default=Storage.serialize_datetime)

    # Custom function to serialize datetime objects 
    def serialize_datetime(obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")