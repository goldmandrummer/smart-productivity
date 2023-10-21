from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Task:
    id: int
    name: str
    due_date: datetime
    duration: int
    priority: int
    is_recurring: bool
    tags: List[str]
