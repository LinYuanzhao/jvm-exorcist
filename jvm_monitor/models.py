"""""
数据模型定义

"""""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ProcessInfo:
    pid: int
    name: str
    start_time: int
    memory_mb: int

    @property
    def formatted_start_time(self) -> str:
        return datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def from_line(cls, line: str) -> Optional["ProcessInfo"]:
        parts = line.strip().split("|")
        if len(parts) != 4:
            return None

        try:
            pid = int(parts[0])
            name = parts[1]
            start_time = int(parts[2])
            memory_mb = int(parts[3])
            return cls(pid=pid, name=name, start_time=start_time, memory_mb=memory_mb)
        except ValueError:
            return None

