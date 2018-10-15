# Class to define the structure of the scheduler

class Scheduler:
    def __init__(self):
        self.time = 0
        self.ready_queue = []
        self.cpu = []
        self.io = []
        self.context_switch = False
        self.completed = []
        self.utilization = 0

    def get_next_process(self):
        if self.ready_queue:
            earliest_arrival = self.ready_queue[0] # Get process with earliest arrival time
            for i in range(1, len(self.ready_queue)):
                if self.ready_queue[i].arrival_time < earliest_arrival.arrival_time:
                    earliest_arrival = self.ready_queue[i]
                
                elif self.ready_queue[i].arrival_time == earliest_arrival.arrival_time:
                    earliest_arrival = self.ready_queue[i] if (self.ready_queue[i].name < earliest_arrival.name) else earliest_arrival
            return earliest_arrival
        else:
            return False

    def display_ready_queue(self):
        print("Process          CPU Burst")
        if self.ready_queue:
            for proc in self.ready_queue:
                print(str(proc) + "                 " + str(proc.current_burst))
        else:
            print("[Empty]")
        print()

    def display_io_queue(self):
        print("Process          Remaining I/O Time")
        if self.io:
            for proc in self.io:
                print(str(proc) + "                 " + str(proc.current_io))
        else:
            print("[Empty]")
        print()

    def display(self):
        print("Current time: " + str(self.time))
        try:
            print("Now Running: " + str(self.cpu[0]))
        except IndexError:
            print("Now Running: IDLE")
        print("--------------------------------------------")
        self.display_ready_queue()
        self.display_io_queue()
        print()

    def load_cpu(self, proc):
        del self.ready_queue[self.ready_queue.index(proc)]
        self.cpu.append(proc)

    def load_io(self, proc):
        self.cpu = []
        self.io.append(proc)

    def load_ready_queue(self, proc):
        del self.io[self.io.index(proc)]
        self.ready_queue.append(proc)

    def advance_time(self):
        self.time = self.time + 1

    def advance_wait_time(self):
        for proc in self.ready_queue:
            proc.wait_time += 1
    
    def clear_cpu(self):
        self.cpu = []

    def compute_avg(self, type):
        total = 0
        if type == "wait":
            for proc in self.completed:
                total += proc.wait_time
            return("Average wait time: " + str(total/8))
        elif type == "tt":
            for proc in self.completed:
                total += proc.ta_time
            return("Average turnaround time: " + str(total/8))
        else:
            for proc in self.completed:
                total += proc.resp_time
            return("Average response time: " + str(total/8))

    def display_results(self):
        results_string = ""
        results_string += "Process     RT         WT           TT\n-----------------------------------------\n"
        for proc in self.completed:
            results_string += str(proc) + "     -    " + str(proc.resp_time) + "     -    " + str(proc.wait_time)+ "     -    " + str(proc.ta_time) + "\n"
        results_string += "CPU Utilization: {:.4f}".format((self.utilization/self.time) * 100)
        return results_string 