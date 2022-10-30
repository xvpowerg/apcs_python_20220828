class MyDeque:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity        
    def isEmpty(self):
        return len(self.queue)==0
    def isFull(self):
        return len(self.queue)==self.capacity
    def addFront(self, data):
        if(self.isFull()):
            print("佇列已滿!")
            return 
        self.queue.insert(0, data)
    def addRear(self, data):
        if(self.isFull()):
            print("佇列已滿!")
            return 
        self.queue.append(data)
    def delFront(self):
        if(self.isEmpty()):
            print("佇列為空!")
            return None
        return self.queue.pop(0)
    def delRear(self):
        if(self.isEmpty()):
            print("佇列為空!")
            return None
        return self.queue.pop() 
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)

deq = MyDeque(4)

s = 64
for i in range(6):
    s+=1
    print('加入', chr(s))
    if(i%2==0):
        deq.addFront(chr(s))
    else:
        deq.addRear(chr(s))
    print(deq)

for j in range(6):
    if(j%2==0):
        item = deq.delFront()
    else:
        item = deq.delRear()
    if(item):
        print("取出:", item)
    print(deq)
