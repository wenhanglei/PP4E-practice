"spawn threads until you type 'q'"
import _thread
import sys

def child(tid):
    mutex.acquire()
    print('Hello from thread '+str(tid), end='')
    mutex.release()
def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break

mutex = _thread.allocate_lock()
parent()
