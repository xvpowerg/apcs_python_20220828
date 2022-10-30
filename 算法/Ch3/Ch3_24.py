'''
使用枚舉法列舉 [A, B, C, D, E, F] 中取三個元素的所有組合
使用 continue 減少測試數量
'''
count = 0
c = 65
for i in range(0,6):
    for j in range(0,6):
        if j <= i:
            continue
        for k in range(0,6):
            if k <= j:
             continue
            count+=1
            print(f"{count:2d} [{chr(c+i)},{chr(c+j)},{chr(c+k)}]")
