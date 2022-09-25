v = input("F範圍")
print(type(v))
max = int(input("F範圍"))
num1,num2 = 1,1
print(num1,num2,sep=',',end='')
next = num1 + num2
while(next < max):
    print(f",{next}",end = "")
    num1 = num2
    num2 = next
    next = num1 + num2
