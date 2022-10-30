'''
使用枚舉法將[A, B, C, D, E] 所有的排列，一一列舉出來
使用 continue 減少測試數量
'''

count = 0
c = 65
for i in range(0,5):
    for j in range(0,5):
        if (j==i):
            continue
        for k in range(0,5):
            if (k==j or k==i):
                continue
            for l in range(0,5):
                if (l==k or l==j or l==i):
                    continue
                for m in range(0,5):
                    if(m==l or m==k or m==j or m==i):
                        continue
                    count+=1
                    print(f"[{count:3d} { chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+l)},{chr(c+m)}]")
