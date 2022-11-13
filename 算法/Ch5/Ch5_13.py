def showdata(data_list):
    print('[', end='')
    for i in range(len(data_list)):
        print(data_list[i],end=' ')
    print(']')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self, student2):
        if self.age<student2.age:
            return True
        else:
            return False
    def __gt__(self, student2):
        if self.age>student2.age:
            return True
        else:
            return False
    def __str__(self):
        return '%5s(%d,%.1f)'%(self.name,self.age,self.gpa)

def interpolation_search(data,val):
    low, high = 0, len(data)-1
    mid = -1
    while low < high:
        mid=low+(high-low)*(val-data[low].age)//(data[high].age-data[low].age)          #內插法公式
        if(mid<low or mid>high):
            return -1
        if val < data[mid].age:
            print('%d 介於位置 %d[%s]及內插值 %d[%s]，找左半邊' \
                  %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val > data[mid].age:
            print('%d 介於內插值 %d[%s] 及位置 %d[%s]，找右半邊' \
                  %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1

data=[Student('Amy', 15, 4.2),
      Student('Bill', 16, 3.8),
      Student('Chris', 13, 4.0),
      Student('David', 19, 4.8),
      Student('Ed', 17, 2.6)]

data.sort()
print('資料內容：', end='')
showdata(data)

while True:
    val=int(input('請輸入搜尋年紀，輸入-1結束：'))
    if val==-1:
        break
    pos=interpolation_search(data,val)
    if pos==-1:
         print('##### 年紀[%d]學生不存在 #####' %val)
    else:
        print('在第 %2d個位置找到 [%s]' %(pos+1,data[pos]))
