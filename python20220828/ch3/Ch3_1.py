ch = int(input("請輸入國文成績:"))
ma = int(input("請輸入數學成績:"))
en = int(input("請輸入英文成績:"))
total = ch + ma + en
print("總成績:",total)
print(f"平均分數{total / 3:.2f}")

"""
names = ["國文","數學","英文","物理"]
total = 0
for n in names:
   total += int(input(f"請輸入{n}成績:"))
print("總成績:",total)
print(f"平均分數{total / len(names):.2f}")
"""   

