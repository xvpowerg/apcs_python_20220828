cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
print('氣泡排序法,原始資料為：', cars, sep='')

n = len(cars)

for i in range(1, n):                                           #掃描次數
    for j in range(n-i):
        if cars[j]>cars[j+1]:                                   #比較,交換的次數
            cars[j],cars[j+1]=cars[j+1],cars[j]                 #比較相鄰資料,如果第一筆資料較大則交換
    print('第 %d 次掃描後的結果是：' %i,end='')                 #把各次掃描後的結果印出
    print(cars)
	
print('氣泡排序之後的資料為：', cars)
