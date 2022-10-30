class Employee:
    num = 0
    def __init__(self, name, salary):
        Employee.num += 1
        self.eid = Employee.num
        self.name = name
        self.salary = salary
    def __str__(self):
        return '%s(%d)' %(self.name,self.eid)
        
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self): 
        self.head = None        
    def add(self, emp):
        newNode = Node(emp)
        if self.head==None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next: 
            ptr = ptr.next
        ptr.next = newNode
    def getIndex(self, eid):
        ptr = self.head
        i = 0
        while ptr:
            if(ptr.data.eid==eid):
                break
            ptr = ptr.next
            i += 1
        else:
            i=-i
        return i        
    def getNode(self, index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
            if(ptr==None):
                break
        return ptr
    def delete(self, index):
        if(index==0):
            self.head=self.head.next
            return
        preNode = self.getNode(index-1)
        delNode = preNode.next
        preNode.next = delNode.next
    def count(self):
        count = 0
        if self.head==None:
            return 0
        ptr = self.head
        while ptr.next: 
            ptr = ptr.next
            count += 1
        return count        
    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=' ')
            ptr = ptr.next
        print()

print('======新增員工======')
empLL = LinkedList()
empLL.add(Employee('Sean', 50000))
empLL.add(Employee('David', 60000))
empLL.add(Employee('Amy', 30000))
empLL.add(Employee('Ivy', 45000))
empLL.add(Employee('Nicole', 80000))
empLL.print()
print('======2號員工離職======')
pos = empLL.getIndex(2)
if(pos>=0):
    empLL.delete(pos)
empLL.print()

print('======反向列印======')
for i in range(empLL.count(), -1, -1):
    print(empLL.getNode(i).data, end =' ')
