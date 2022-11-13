import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='') #第i次5 + j+1
        print()

def interpolation_search(data,val):
    low, high = 0, len(data)-1
    mid = -1
    while low < high:
        mid=low+(val-data[low])*(high-low)//(data[high]-data[low])          #內插法公式
        if(mid<low or mid>high):
            return -1
        if val < data[mid]:
            print('%d 介於位置 %d[%3d]及內插值 %d[%3d]，找左半邊' \
                  %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val > data[mid]:
            print('%d 介於內插值 %d[%3d] 及位置 %d[%3d]，找右半邊' \
                  %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1

data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)

data.sort()
print('資料內容：')
showData(data)

while True:
    val=int(input('請輸入搜尋鍵值(1-100)，輸入-1結束：'))
    if val==-1:
        break
    pos=interpolation_search(data,val)
    if pos==-1:
         print('##### [%3d]不存在 #####' %val)
    else:
        print('在第 %2d個位置找到 [%3d]' %(pos+1,data[pos]))
