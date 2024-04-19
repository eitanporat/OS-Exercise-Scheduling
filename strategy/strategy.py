from abc import ABC
from typing import Any, List
from process import Process, execute_process

class Strategy(ABC):
    processes: List[Process]
    name: str

    def __init__(self, name):
        self.name = name

    def execute(self, processes: List[Process]) -> None:
        self.processes = processes
        self.remaining_processes = []
        self.to_process = self.processes.copy()
        self.turnarround = 0

    def calculate_turnarround_time(self) -> float:
        turnaround_average = 0

        for process in self.processes:
            turnaround_average += process.end_time - process.start_time

        return turnaround_average / len(self.processes)

    def print(self) -> None:
        print(f"{self.name}: mean turnaround = {self.calculate_turnarround_time()}")

    def sort_function(self, process: Process) -> Any:
        raise NotImplementedError('Sort function is not implemented')

    def choose_process(self) -> Process:
        self.remaining_processes = sorted(self.remaining_processes, key=self.sort_function)
        return self.remaining_processes[0]

    def finish(self, process: Process) -> None:
        self.turnarround += process.end_time - process.start_time
        self.to_process.remove(process)
        self.remaining_processes.remove(process)

class PreemptiveStrategy(Strategy):
    def __init__(self, name: str, clock_cycle : int=1):
        super().__init__(name)
        self.clock_cycle = clock_cycle

    def execute(self, processes: List[Process]) -> None:
        super().execute(processes)
        time = 0

        while self.to_process:
            self.remaining_processes += [process for process in self.to_process if time - self.clock_cycle < process.start_time <= time]
            if self.remaining_processes:
                process = self.choose_process()
                process = execute_process(process, time, self.clock_cycle)
                if process.remaining_service_time == 0:
                    self.finish(process)

            time += self.clock_cycle

class NonPreemptiveStrategy(Strategy):
    def __init__(self, name: str):
        super().__init__(name)

    def execute(self, processes: List[Process]) -> None:
        super().execute(processes)

        time = 0
        while self.to_process:
            self.remaining_processes = [process for process in self.to_process if process.start_time <= time]

            if self.remaining_processes:
                process = self.choose_process()
                self.finish(execute_process(process, time, process.service_time))
                time += process.service_time
            else:
                time += 1
