from process import Process
from .strategy import PreemptiveStrategy

class RoundRobin(PreemptiveStrategy):
    def __init__(self):
        super().__init__("RR", clock_cycle=2)
        
    def choose_process(self) -> Process:
        process = self.remaining_processes[0]
        self.remaining_processes = self.remaining_processes[1:] + [process]
        return process
