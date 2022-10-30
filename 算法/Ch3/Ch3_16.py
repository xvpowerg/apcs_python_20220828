class Queue():
    def __init__(self):
        self.my_queue = []                 # 使用串列模擬

    def enqueue(self, data):
        self.my_queue.append(data)

    def dequeue(self):
        return self.my_queue.pop(0)

    def size(self):
        return len(self.my_queue)
    
    def isEmpty(self):
        return self.my_queue == []

queue = Queue()
people = ['Amy', 'David', 'Sean']
for person in people:
    queue.enqueue(person)
    print('將 %s 排入佇列' %person)

print('佇列中有%d個人' %queue.size())
while not queue.isEmpty():
    print(queue.dequeue())
