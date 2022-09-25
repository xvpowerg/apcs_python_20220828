height = float(input("身高公分:"))
weight = int(input("體重公斤:"))
bmi = weight / ((height/100) ** 2)
print("bmi:",bmi)
print("bmi:%.2f"%(bmi))
print(f"bmi:{bmi:.2f}")

