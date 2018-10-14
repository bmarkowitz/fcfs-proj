from data import *
import scheduler

# All processes activated at time 0
scheduler = scheduler.Scheduler()

scheduler.ready_queue.insert(0, p1)
scheduler.ready_queue.insert(0, p2)
scheduler.ready_queue.insert(0, p3)
scheduler.ready_queue.insert(0, p4)
scheduler.ready_queue.insert(0, p5)
scheduler.ready_queue.insert(0, p6)
scheduler.ready_queue.insert(0, p7)
scheduler.ready_queue.insert(0, p8)

while(True):

    if scheduler.io:
        i = 0
        while(True):
            try:
                if scheduler.io[i]:
                    proc = scheduler.io[i]
                    if proc.io_burst_is_complete():
                        proc.set_next_io()
                        scheduler.load_ready_queue(proc)
                    else:
                        proc.use_io_burst()
                        i += 1
            except IndexError:
                break

    if scheduler.ready_queue and not scheduler.cpu:
        next_proc = scheduler.get_next_process()
        scheduler.load_cpu(next_proc)
        scheduler.display()

    if scheduler.cpu:
        current_proc = scheduler.cpu[0]
        if current_proc.cpu_burst_is_complete():
            try_set = current_proc.set_next_cpu()
            next_proc = scheduler.get_next_process()
            if try_set:
               current_proc.set_arrival_time(scheduler.time) 
               scheduler.load_io(current_proc)
               if next_proc:
                   scheduler.clear_cpu
                   scheduler.load_cpu(next_proc)

            else:
                scheduler.clear_cpu()
                if next_proc:
                    scheduler.load_cpu(next_proc)
            scheduler.context_switch = True

            if next_proc:
                next_proc.use_cpu_burst()
        
        else:
            current_proc.use_cpu_burst()

    if not scheduler.cpu and not scheduler.ready_queue and not scheduler.io:
        scheduler.display()
        break
    
    if scheduler.context_switch:
        scheduler.display()
        scheduler.context_switch = False

    scheduler.advance_time()