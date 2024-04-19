from typing import Tuple
from process import Process, execute_process
from .strategy import NonPreemptiveStrategy, PreemptiveStrategy

class LastComeFirstServePreemptive(PreemptiveStrategy):
    def __init__(self) -> None:
        super().__init__("LCFS (P)")

    def sort_function(self, process: Process) -> Tuple[int, int]:
        return (-process.start_time,  process.remaining_service_time)

class LastComeFirstServeNonPreemptive(NonPreemptiveStrategy):
    def __init__(self) -> None:
        super().__init__("LCFS (NP)")

    def sort_function(self, process: Process) -> Tuple[int, int]:
        return (-process.start_time,  process.remaining_service_time)
