from data import *

# Function to complete a CPU burst
def use_cpu_burst(proc):
    proc.current_burst -= 1 # Decrement

def use_io_burst(proc):
    proc.current_io -= 1 # Decrement io

def cpu_burst_is_complete(proc):
    if proc.current_burst == 0: return True
    else: return False

def io_burst_is_complete(proc):
    if proc.current_io == 0: return True
    else: return False

time = 0
ready_queue  = [] # Accumulating wait time
executing_queue = [] # Using current cpu time
io_queue = [] # Using current io time
complete_queue = []

# All processes activated at time 0
ready_queue.insert(0, p8)
ready_queue.insert(0, p7)
ready_queue.insert(0, p6)
ready_queue.insert(0, p5)
ready_queue.insert(0, p4)
ready_queue.insert(0, p3)
ready_queue.insert(0, p2)
ready_queue.insert(0, p1)

while(True):

    print(complete_queue)

    if len(ready_queue) == 8: # Condition to get process for very beginning
        proc = ready_queue.pop()
        executing_queue.insert(0, proc)
        use_cpu_burst(proc) # Uses up one time unit of CPU burst
        time += 1
        continue
    
    while(True):
        if (executing_queue):
            proc = executing_queue[0]
            if (cpu_burst_is_complete(proc)):
                print(str(proc) + ": burst complete at time " + str(time))
                proc.set_arrival_time(time)
                proc = executing_queue.pop()
                io_queue.insert(0, proc)
            else:
                use_cpu_burst(proc)
                # time += 1
            break
        else:
            try:
                earliest_arrival = ready_queue[0]
                for i in range(1, len(ready_queue)):
                    if ready_queue[i].arrival_time < earliest_arrival.arrival_time:
                        earliest_arrival = ready_queue[i]
                
                proc_to_exec = ready_queue.pop(ready_queue.index(earliest_arrival))
                executing_queue.insert(0, earliest_arrival)
                continue
            except IndexError:
                break

    if (io_queue):
        for io_queue_process in io_queue:
            if io_burst_is_complete(io_queue_process):
                proc = io_queue.pop(io_queue.index(io_queue_process))
                try:
                    proc.set_next_cpu()
                    proc.set_next_io() 
                    ready_queue.insert(0, proc)
                except IndexError:
                    print("This process is complete")
                    complete_queue.append(proc)
                    continue
            else:
                use_io_burst(io_queue_process)

        # time += 1

    if not ready_queue:
        for io_queue_process in io_queue:
            if io_burst_is_complete(io_queue_process):
                proc = io_queue.pop(io_queue.index(io_queue_process))
                try:
                    proc.set_next_cpu()
                    proc.set_next_io() 
                    ready_queue.insert(0, proc)
                except IndexError:
                    print("This process is complete")
                    complete_queue.append(proc)
                    continue
            else:
                use_io_burst(io_queue_process)

    if len(complete_queue) == 8:
        break  

    time += 1

print(time)

    


