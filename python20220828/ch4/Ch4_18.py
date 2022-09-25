'''
list1 = ['a','b','c']
print("附加之前:",list1)
print("附加之前長度:",len(list1))
list1.append(["def","ghij"])
print("附加之後:",list1)
print("附加之長度:",len(list1))
print("附加元素:",list1[3])
'''

list1 = ['a','b','c']
print("擴展之前:",list1)
print("擴展之前長度:",len(list1))
#list1.extend(["def","ghij"])
list1 += ["def","ghij"]
print("擴展之後:",list1)
print("擴展之長度:",len(list1))
print("擴展元素:",list1[3])
