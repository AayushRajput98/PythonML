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
    k.setName("one")
    k.join(2)
    k2.start()
    k2.setName("two")
    k2.join()

except Exception as e:
    print(e)