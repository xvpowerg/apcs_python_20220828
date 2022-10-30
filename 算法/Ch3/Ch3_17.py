from queue import Queue

q = Queue(3)
people = ['Amy', 'David', 'Sean', 'Nicole']
for person in people:
    if q.full():
        print('佇列已滿')
    else:   
        q.put(person)
        print('將 %s 排入佇列' %person)   
print('佇列中有%d個人' %q.qsize())
print(q.queue)

for i in range(4):
    if q.empty():
        print('佇列為空')
    else:   
        print(q.get())
print('佇列中有%d個人' %q.qsize())
print(q.queue)
