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
        if self.gpa<student2.gpa:
            return True
        else:
            return False
    def __gt__(self, student2):
        if self.gpa>student2.gpa:
            return True
        else:
            return False
    def __str__(self):
        return '%5s(%d,%.1f)'%(self.name,self.age,self.gpa)

def bin_search(data, score):
    low, high = 0, len(data)-1
    mid = -1
    while not low>high:
        mid=(low+high)//2
        if score>data[mid].gpa:
            print('%d 介於最小值 %2d[%s]及中間值 %2d[%s]，找左半邊' \
                   %(score,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif score<data[mid].gpa:
            print('%d 介於中間值 %2d[%s]及最大值 %2d[%s]，找右半邊' \
                  %(score,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1

data=[Student('Amy', 15, 4.2),
      Student('Bill', 16, 3.8),
      Student('Chris', 13, 4.0),
      Student('David', 19, 4.8),
      Student('Ed', 17, 2.6)]

data.sort(reverse=True)
print('資料內容：', end='')
showdata(data)

while True:
    score=float(input('請輸入搜尋成績，輸入-1結束：'))
    if score == -1.0:
        break
    pos=bin_search(data,score)
    if pos==-1:
        print('##### 沒有成績[%.1f]的學生 #####' %score)
    else:
        print('在第%2d個位置找到學生[%s]' %(pos+1, str(data[pos])))
