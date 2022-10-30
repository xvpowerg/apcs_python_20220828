class Customer:
    def __init__(self, name, trxType, amount):
        self.name = name
        self.trxType = trxType
        self.amount = amount
    def __str__(self):
        return '{0}{1}{2}元'.format(self.name,self.trxType,self.amount)

class ServQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity        
    def isEmpty(self):
        return len(self.queue)==0
    def isFull(self):
        return len(self.queue)==self.capacity
    def enqueue(self, data):
        if(self.isFull()):
            print("隊伍已滿!")
            return
        self.queue.append(data)        
        print("%s排入隊伍"%data.name)
    def dequeue(self):
        if(self.isEmpty()):
            print("隊伍為空!")
            return None
        return self.queue.pop(0)    
    def size(self):
        return len(self.queue)

servQueue = ServQueue(5)
customers = [Customer('Sean','存款',1000),
             Customer('David','提款',2000),
             Customer('Amy','存款',3000),
             Customer('Ed','存款',4000),
             Customer('Nicole','提款',5000),
             Customer('Douglas','存款',4000),
             Customer('Elizabeth','提款',6000)]

for cus in customers:
    servQueue.enqueue(cus)

for i in range(servQueue.size()):    
    print(servQueue.dequeue())
