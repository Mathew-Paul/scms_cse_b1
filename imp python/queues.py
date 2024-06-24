class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
    
    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
        else:
            print("Queue Overflow: Cannot enqueue item, queue is full")
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue Underflow: Cannot dequeue item, queue is empty")
            return None
    
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print("Queue is empty, no front element")
            return None
    
    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            print("Queue is empty, no rear element")
            return None
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.max_size
    
max_size=int(input("Enter the size of stack:"))
queue=Queue(max_size)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Is empty?", queue.isEmpty())  
print("Is full?", queue.isFull())

print("Front:", queue.front())  
print("Rear:", queue.rear())   
print("Dequeue:", queue.dequeue()) 

