class Ship:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items=[]
        self.weight=0
        self.value=0    
    def put(self, item):
        if self.weight+item.weight>capacity:
            return False
        else:
            self.items.append(item)
            self.weight += item.weight
            self.value += item.value
            return True
    def print(self):
        print('[', end='')
        for item in self.items:
            print(item, end=' ')
        print(']:', self.value)

class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.unitValue = value/weight
    def __lt__(self, other):
        return self.unitValue < other.unitValue
    def __str__(self):
        return '(%d,%d)'%(self.weight, self.value)

treasures = [50,160,20,100,20,60,90,120,150,30]
values = [40,10,50,60,50,20,50,30,60,30]
capacity = 500

ship = Ship(capacity)
items = []
for w,v in zip(treasures, values):
    items.append(item(w,v))
sortedItems = sorted(items, reverse=True)
for i in sortedItems:
    if not ship.put(i):
        break
ship.print()
