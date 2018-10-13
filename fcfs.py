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

def display_ready_queue():
    print("Process          CPU Burst")
    if ready_queue:
        for proc in ready_queue:
            print(str(proc) + "          " + str(proc.current_burst))
    else:
        print("[Empty]")

def display_io_queue():
    print("Process          Remaining I/O Time")
    if io_queue:
        for proc in io_queue:
            print(str(proc) + "         " + str(proc.current_io))
    else:
        print("[Empty]")

def display():
    print("Current time: " + str(time))
    try:
        print("Now Running: " + str(executing_queue[0]))
    except IndexError:
        print("Now Running: IDLE")
    print("--------------------------------------------")
    display_ready_queue()
    display_io_queue()
    print()
    print()

def get_next_process():
    try:
        earliest_arrival = ready_queue[0] # Get earliest arrival time
        for i in range(1, len(ready_queue)):
            if ready_queue[i].arrival_time < earliest_arrival.arrival_time:
                earliest_arrival = ready_queue[i]
            
            elif ready_queue[i].arrival_time == earliest_arrival.arrival_time:
                earliest_arrival = ready_queue[i] if (ready_queue[i].name < earliest_arrival.name) else earliest_arrival
            
            
        if earliest_arrival.arrival_time <= time:        
            proc_to_exec = ready_queue.pop(ready_queue.index(earliest_arrival)) # Remove from ready queue
            executing_queue.insert(0, proc_to_exec) # Add to executing queue
            
            display()
        
    except IndexError:
        pass

time = 0
ready_queue  = [] # Accumulating wait time
executing_queue = [] # Using current cpu time
io_queue = [] # Using current io time
complete_queue = []
cpu_idle = False

# All processes activated at time 0
ready_queue.insert(0, p1)
ready_queue.insert(0, p2)
ready_queue.insert(0, p3)
ready_queue.insert(0, p4)
ready_queue.insert(0, p5)
ready_queue.insert(0, p6)
ready_queue.insert(0, p7)
ready_queue.insert(0, p8)


while(True):

    if ready_queue and not executing_queue:
        get_next_process()

    if (io_queue):
        removed = []
        for io_queue_process in io_queue:
            if io_burst_is_complete(io_queue_process): # Check if io is complete
                removed.append(io_queue_process) # Add to "to be removed" array
                io_queue_process.set_next_io()  # Try to set next io burst
                ready_queue.insert(0, io_queue_process) # Insert into ready queue            
                continue
            else:
                use_io_burst(io_queue_process) # If not complete, use an io time unit

        if removed:
            for proc in removed:
                del io_queue[io_queue.index(proc)]

    if executing_queue:
        proc = executing_queue[0] # Get process on CPU
        if (cpu_burst_is_complete(proc)): # If burst is complete
            try_set = proc.set_next_cpu()
            
            if not try_set:
                proc = executing_queue.pop() # Remove from CPU
                proc.ta_time = time
                complete_queue.append(proc)
                get_next_process()
            
            else:
                proc.set_arrival_time(time) # Set time to arrive in ready queue from io
                proc = executing_queue.pop() # Remove from CPU
                io_queue.insert(0, proc) # Insert into io
                
                get_next_process()
                # use_io_burst(proc) # Immediately use an io time unit
                
            continue
        else:
            use_cpu_burst(proc)
            cpu_idle = False

    if not executing_queue and not cpu_idle:
        cpu_idle = True
        display()

    if len(complete_queue) == 8:
        break  

    time += 1