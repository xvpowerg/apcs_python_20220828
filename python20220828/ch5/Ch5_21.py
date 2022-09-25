class Employee:
    company = "巨匠電腦"
    phone = '02 2314537'
    count = 0
    def __init__(self,name,salary = 20000):
        self.name = name
        self.salary = salary
        Employee.count+=1
    def printInfo(self):
        print("姓名:",self.name)
        print("薪水:",self.salary)
        print("電話:",Employee.phone)
    def getTotal():
        return Employee.count
    
emp1 = Employee("Sean",50000)
emp2 = Employee("Tom",60000)
emp3 = Employee("Iris",40000)

print(Employee.getTotal())
