num = int(input("輸入個數:"))
arr = [0]*num
for i in range(num):
    arr[i] = int(input(f"輸入第{i+1}個整數:"))
    
for j in range(num-1):
    if arr[j] >= arr[j+1]:
        print("不是遞增陣列")
        break
else:
  print("遞增陣列")


for k in range(num-1):
    if arr[k] * arr[k+1] >=0:
        print("不是正負交錯")
        break
else:
    print("正負交錯陣列")
    
print(arr)
