def fi(n):
    result = 1
    for i in range(n, 0, -1):
        #print(i, "*", end=' ') if i>1 else print(i)
        result *= i
    return result

def print_process(N, n):
    for i in range(N, n, -1):
        print('%d*' %i, end='')
    print('%d!='%n, end='') if n>1 else print(1)
    
def fir(n):
    #print_process(N, n)
    if n==1:        
        return 1
    else:
        return n * fir(n-1)
    


N = eval(input("請輸入階乘數 : "))#eval 自動轉型成可以做計算的數值
#print("%d! = %d" %(N,fi(N)))
print("%d! = %d" %(N,fir(N)))
