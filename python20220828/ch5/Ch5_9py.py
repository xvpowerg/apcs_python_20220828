import random

ans = random.randint(1,5)
print(ans)
guess = int(input("請猜1~5的數字:"))
if guess == ans:
    print("答對了")
else:
    print("錯了")
