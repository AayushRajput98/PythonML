import threading
import time
class myThread (threading.Thread):
    def run(self):
        count = 0
        while count<5:
            time.sleep(2)
            count+=1
            print(count)
            print(self.name)
try:
    k=myThread()
    k2=myThread()
    k.start()
    print(k.setName("one"))
    k2.start()
    print(k2.setName("two"))
except Exception as e:
    print(e)