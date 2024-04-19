from dataclasses import dataclass

@dataclass
class Process:
    start_time: int
    service_time: int
    end_time: int
    remaining_service_time: int

def execute_process(process, current_time, duration):
    process.remaining_service_time = max(0, process.remaining_service_time - duration)
    process.end_time = current_time + duration

    return process