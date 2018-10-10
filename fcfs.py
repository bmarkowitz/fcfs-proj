from data import *

# Function to complete a CPU burst
def complete_cpu_burst(proc):
    while proc.current_burst < 0:
        proc.current_burst -= 1 # Decrement

time = 0
ready_queue  = [] # Accumulating wait time
executing_queue = [] # Using current cpu time
io_queue = [] # Using current io time

# All processes activated at time 0
ready_queue.insert(0, p1)
ready_queue.insert(0, p2)
ready_queue.insert(0, p3)
ready_queue.insert(0, p4)
ready_queue.insert(0, p5)
ready_queue.insert(0, p6)
ready_queue.insert(0, p7)
ready_queue.insert(0, p8)