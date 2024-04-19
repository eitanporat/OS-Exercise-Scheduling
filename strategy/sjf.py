from process import Process
from .strategy import PreemptiveStrategy

class ShortestJobFirst(PreemptiveStrategy):
    def __init__(self):
        super().__init__("SJF")

    def sort_function(self, process: Process) -> int:
        return process.remaining_service_time
