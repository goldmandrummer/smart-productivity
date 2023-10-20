from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    name: str
    due_date: datetime
    duration: int
    priority: int
    is_recurring: bool
