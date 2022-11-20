data=[[1,(2,1)],[1,(3,4)],
      [2,(1,1)],[2,(4,2)],
      [3,(1,4)],[3,(5,5)],
      [4,(2,2)],[4,(5,3)],
      [5,(3,5)],[5,(4,3)]]

graph = {}                                          #圖形dict宣告
print('圖形的鄰接串列內容：')
print('----------------------------------')
for i in range(1,6):
    graph[i] = []                                   #每個頂點對應一個空的list

for j in range(len(data)):    
    graph[data[j][0]].append(data[j][1])
    #print(graph)

for k in graph:                                     #走訪圖形陣列
    print('頂點 %d =>' %k, end='')                  #把頂點值列印出來
    for l in graph[k]:
        print('(%d,%d) ' %l, end='')                #列印相鄰頂點
    print()
