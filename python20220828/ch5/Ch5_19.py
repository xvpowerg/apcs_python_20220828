class Person:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello,",self.name)
        
p1 = Person("Amy")
greet = p1.sayHello #當作是一個 屬性內放了一個function物件
greet()

Person.sayHello(p1)

