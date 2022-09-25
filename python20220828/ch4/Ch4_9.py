list1 = [1,2,3,4,5]

def sq(x):
    return x ** 2
list2 = map(sq,list1)
print(list1)
print(list(list2))

list2 = map(lambda x:x**2 ,list1)
print(list(list2))

list1 = [1,2,3,5,8,13,21,34,55,89]
print(list1)
list2 = filter(lambda x : x%2 != 0,list1)
print(list2)
print(list(list2))

