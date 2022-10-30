'''
程式範例：質數驗證
'''
#檢查是否為質數
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
n = int(input("輸入一個正整數"))
if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")

primeNums=[]
#顯示小於等於n的質數
for j in range(2 , n + 1):
    if is_prime(j):
        primeNums.append(j);       
print(f"小於等於{n}的質數:",primeNums)    
