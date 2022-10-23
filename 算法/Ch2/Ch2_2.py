from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列
print("循序讀取:", end='')
for data in x:
    print(data, end=', ')               # 循序讀取

print("\n索引讀取:", end='')
for i in range(len(x)):
    print(x[i], end=', ')               # 使用索引隨機讀取

print("\n索引2插入100")
x.insert(2, 100)                        # 指定位置插入元素
print(x)

print("附加100") 
x.append(100)                           # 附加元素於陣列尾端
print(x)

print("修改索引2為20") 
x[2] = 20                              # 修改指定索引元素
print(x)

print("刪除20") 
x.remove(20)                            # 刪除指定元素
print(x)

n = x.pop()                             # 彈出元素
print('彈出元素:', n)
print(x)

n = x.pop(2)                            # 彈出元素
print('彈出索引2:', n)
print(x)

i = x.index(35)                         # 取得元素索引
print("35位於索引%d" %i)
