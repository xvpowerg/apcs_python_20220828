def gcd_it(m, n):
    while(n!=0):
        print(f'gcd({m},{n})=', end='')
        r = m%n
        m = n
        n = r
    return m
def gcd_rc(m, n):
    print('gcd(%d,%d)='%(m,n), end='')
    if n==0:
        return m
    else:
        return gcd_rc(n, m%n)

n1 = int(input('num1='))
n2 = int(input('num2='))
if(n1<n2):
    n1,n2 = n2,n1
#gcd = gcd_it(n1, n2)
gcd = gcd_rc(n1, n2)
print(gcd)
