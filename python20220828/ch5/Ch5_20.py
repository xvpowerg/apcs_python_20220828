class Employee:
    company = "巨匠電腦"
    phone = '02 2314537'
    def __init__(self,name,salary = 20000):
        self.name = name
        self.salary = salary
    def printInfo(self):
        print("姓名:",self.name)
        print("薪水:",self.salary)
        print("電話:",Employee.phone)
emp1 = Employee("Sean",50000)
emp2 = Employee("David")
print(Employee.company)
emp1.printInfo()
emp2.printInfo()

emp1.name = "Iris"
emp1.printInfo()
emp2.printInfo()
print("============================")
Employee.phone = "07 5591633" #類別屬性對於物件來說記憶體共享

emp1.printInfo()
emp2.printInfo()
