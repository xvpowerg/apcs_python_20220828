def showdata(data_list):
    for i in range(len(data_list)):
        print('%3d' %data_list[i],end='')
    print()

data=[16,25,39,63,27,12,8,45]	                # 原始資料 
print('氣泡排序法：原始資料為：')
showdata(data)

n = len(data)

for i in range(1, n):                           #掃描次數
    for j in range(n-i):
        if data[j]>data[j+1]:                   #比較,交換的次數
            data[j],data[j+1]=data[j+1],data[j] #比較相鄰兩數,如果第一數較大則交換
    print('第 %d 次掃描後的結果是：' %i,end='') #把各次掃描後的結果印出
    showdata(data)
	
print('排序後結果為：')
showdata(data)
