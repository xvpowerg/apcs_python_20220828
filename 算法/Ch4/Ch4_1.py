import math
#紀錄小於等於n的質數
def primeList(number):
    primes = []
    for n  in range(2 , number+1):
        for i in primes:
            if n %i == 0:
                break
        else:
            primes.append(n)
    return    primes  
N = int(input("輸入一個正整數"))

pNumbers = primeList(N)
print(f"小於等於{N}的質數:",pNumbers)   
