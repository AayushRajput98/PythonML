class Queue:
    def __init__(self):
        self.q=[]
    def insert(self,element):
        self.q.append(element)
    def remove(self):
        print(self.q.pop(0))
    def print_queue(self):
        for i in self.q:
            print(i,end=" ")
        print()
queue=Queue()
queue.insert(10)
queue.insert(11)
queue.insert(12)
queue.insert(13)
queue.print_queue()
queue.remove()
queue.print_queue()


