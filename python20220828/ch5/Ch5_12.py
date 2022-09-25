num1 = 10
num2 = 0
nums = [1,3,5,7,9]
#print("out" 語法錯誤
try:
    print(num1/num2)    
    nums[100]#例外錯誤
except IndexError:
    print("IndexError ~~~index錯啦")
except ZeroDivisionError:
    print("分母不可為0")
