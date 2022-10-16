a1 = int(input('輸入首項:'))
r = int(input('輸入公比:'))
n = int(input('輸入項數:'))

print('使用For迴圈求等比數列前%d項的和:' %n)
sum1 = 0
for i in range(n):
    ai = a1*r**i
    sum1 += ai
    print(ai, end='\t')
print('=>', sum1)

def getAn(n):
    if(n==1):
        return a1
    else:
        return getAn(n-1)*r
    
sum2 = 0
for i in range(1, n+1):
    ai = getAn(i)
    sum2 += ai
    print(ai, end='\t')
print('=>', sum2)

def getSn(n):
    if(n==1):
        print(a1, end='\t') 
        return a1
    else:
        an = getAn(n)
        print(an, end='\t')        
        return getSn(n-1) + an

print('使用遞迴求等比數列前%d項的和:' %n)
print('=>', getSn(n))
