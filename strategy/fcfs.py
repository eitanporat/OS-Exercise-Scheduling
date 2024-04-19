from process import Process
from .strategy import NonPreemptiveStrategy

class FirstComeFirstServe(NonPreemptiveStrategy):

    def __init__(self) -> None:
        super().__init__("FCFS")

    def sort_function(self, process : Process) -> None:
        return process.start_time
        