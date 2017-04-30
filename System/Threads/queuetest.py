"producer and consumer threads communicating with a shared queue"

import _thread as thread, queue, time

numconsumers = 2
numproducers = 4
nummessages = 4

safeprint = thread.allocate_lock()
dataQueue = queue.Queue(nummessages)

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            msg = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print("consumer %d got message: %s" % (idnum, msg))

def producer(idnum):
    for i in range(nummessages):
        time.sleep(idnum)
        msg = "producer %d ,count = %d" % (idnum, i)
        dataQueue.put(msg)

threads = []
for i in range(numconsumers):
    cons = thread.start_new_thread(consumer,(i,))
    threads.append(cons)

for i in range(numproducers):
    prod = thread.start_new_thread(producer, (i,))
    threads.append(prod)

time.sleep((numproducers-1)*nummessages+1)
print('main thread exit.')




























    
    
    
