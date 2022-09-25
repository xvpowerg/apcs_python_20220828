num =  int(input("請輸入整數:"))
if (num % 2 == 0 and  num % 3 == 0):
    print("是2的倍數也是3的倍數")
elif (num % 2 == 0):    
    print("是2的倍數")
elif (num % 3 == 0):
    print("是3的倍數")
else:
    print("不是2的倍數與3的倍數")
