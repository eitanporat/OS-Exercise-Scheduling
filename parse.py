from process import Process

def parse_file(path: str):
    processes = []
    
    with open(path, 'r') as file: 
        length = int(file.readline().strip())
        
        for line in file.readlines():
            line_split = line.strip().split(",")
            start_time = int(line_split[0])
            service_time = int(line_split[1])
            processes.append(Process(start_time, service_time, 0, service_time))

    return processes

    



