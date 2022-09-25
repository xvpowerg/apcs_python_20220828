def f1(x,y,*z):
    print(len(z))
    print(x,y,z)
f1(1,2)    
f1(1,2,3,4,5,6)    

def f2(x,y,**z):
    print(x,y,z)
f2(1,2,k1=3,k2=4)


def sumFunc(n1,n2,*other):
    s = n1 + n2
    for i in other:
        s += i
    return s

print(sumFunc(1,2))
print(sumFunc(1,2,3,4,5))
print(sumFunc(1,2,3,4,5,6,7,8,9,10))

def personInfo(name,age,**other):    
    print("=====info====")
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":",other[key])
personInfo("Sean",40)
personInfo("David",35,phone="0987654321",company="ibm")
personInfo("Amy",28,email="amy@gmail.com",company="Google",gender='Female')

    
