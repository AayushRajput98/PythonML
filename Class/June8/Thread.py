#User-defined thread
import _thread
import time
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s"%(threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread( print_time, ("Thread One",2,))
    _thread.start_new_thread(print_time, ("Thread Two",4,))
except Exception as e:
    print(e)

while 1:
    pass