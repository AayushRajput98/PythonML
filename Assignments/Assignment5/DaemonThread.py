import threading, time
def d1():
    print("Daemon")  #Exists as soon as non-daemon thread ends
    time.sleep(1)
    print("Exit")
def d2():
    print("Non-Daemon")
    print("Bye")
a=threading.Thread(target=d1,daemon=True)
b=threading.Thread(target=d2)
a.start()
b.start()
