class Employee:
    def __init__(self,name,salary=20000):
        #print(id(self))
        #print("__init__")
        self.name = name
        self.salary = salary
        
    def printInfo(self,title):
         print(title)
         print("Name:",self.name)
         print("Salary:",self.salary)
    

emp1 = Employee("Ken",35000)
emp2 = Employee("Lucy",37000)
#print(id(emp1))
#print(emp1.name)
#print(emp1.salary)
emp1.printInfo("研發部")
emp2.printInfo("業務部")


