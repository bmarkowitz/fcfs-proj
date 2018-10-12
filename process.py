# Class to define the structure of a single process

class Process:
    def __init__(self, bursts, io, name):
        self.bursts = bursts
        self.io = io
        self.name = name
        self.current_burst = bursts[0]
        self.current_io = io[0]
        self.resp_time = 0
        self.wait_time = 0
        self.ta_time = 0
        self.arrival_time = 0

    def __str__(self):
        return "p" + str(self.name)

    def set_next_cpu(self):
        try:
            del self.bursts[0]
            self.current_burst = self.bursts[0]
            return True
        except IndexError:
            return False

    def set_next_io(self):
        try:
            del self.io[0]
            self.current_io = self.io[0]
        except IndexError:
            pass

    def set_arrival_time(self, current_time):
        self.arrival_time = current_time + self.current_io