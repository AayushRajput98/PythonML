import threading
import time
class one(threading.Thread):
    def run(self):
        count=0
        while count<5:
            count+=1
            time.sleep(1)
            print(count)
            print("This is a thread programing")

o1=one();
o2=one();
o1.start()
o2.start()