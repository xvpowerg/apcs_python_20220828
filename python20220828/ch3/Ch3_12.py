h = float(input("身高:"))
w = int(input("體重:"))
bmi = w / ((h/100)**2)
print(f"bmi:{bmi:.2f}")

if bmi > 30:
    print("胖胖")
elif bmi > 25:
    print("過重")
elif bmi > 18.5:
    print("正常")
elif bmi > 0:
    print("過輕")
else:
    print("錯誤")
