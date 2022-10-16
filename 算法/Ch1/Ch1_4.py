def dec_to_bin(num):
    ls = []
    while True:
        num,mod = divmod(num,2)
        ls.append(str(mod))
        if num == 0:
            return "".join(ls[::-1])
        
def dec_to_oct(num):
    ls = []
    if num < 0 : return "-"+ dec_to_bin(abs(num))
    while True:
       num ,mod = divmod(num,8)
       ls.append(str(mod))
       if num == 0:
           return "".join(ls[::-1])
def dec_to_hex(num):
    base = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ls = []
    while True:
        num,mod = divmod(num,16)
        ls.append(base[mod])
        if num == 0:
            return "".join(ls[::-1])
        
testNum = int(input("輸入十進位整數:"))
#print("二進位:",dec_to_bin(testNum))
#print("八進位:",dec_to_oct(testNum))
print("十六進位:",dec_to_hex(testNum))

