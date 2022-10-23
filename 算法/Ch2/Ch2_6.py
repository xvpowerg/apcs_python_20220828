p = [[''] * 5  for i in range(10)]  #10 * 5 的 二維陣列
print(p)

for i in range(len(p)):
    for j in range(len(p[0])):
        p[i][j] = f"({i},{j})"
        
for r in range(len(p)):
    clen = len(p[0])
    for c in range(clen):
        print(p[r][c],end="")
        if c < clen-1:
           print(" ",end="")    
    print()
