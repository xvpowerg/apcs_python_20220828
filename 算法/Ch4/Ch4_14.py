def fib_it(n):
    if n == 0:
        return 0;
    elif n== 1:
        return 1;
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return nextNum

def fib_rc(n):
    if n<=0:
       return 0
    elif n== 1 or n==2:
        return 1
    return fib_rc(n-1) + fib_rc(n-2)

print(f"迴圈:fib({fib_it(6)})")

print(f"迴圈:fib_rc({fib_rc(6)})")
