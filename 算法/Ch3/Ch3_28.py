'''
質數驗證 使用埃拉斯托特尼篩法
'''
import math
def is_prime(num):
    #+1原因必須包含到開根號後的整數 例如:5.2 取整數為5 加1變6 這樣i才會產生2~5的
    for i in range(2,int(math.sqrt(num)+ 1)):
        if num %i==0:
            return False
    return True    
#紀錄小於等於n的質數
def primeList(number):
    primes = []
    for n  in range(2 , number+1):
        if  is_prime(n):
          primes.append(n)
    return primes        
        
N = int(input("輸入一個正整數"))

pNumbers = primeList(N)
print(f"小於等於{N}的質數:",pNumbers)      
