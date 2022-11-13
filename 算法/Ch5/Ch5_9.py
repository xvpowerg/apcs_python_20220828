cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
while True:
    car = input("請輸入車名 Quit離開:")
    if car == 'Quit':
        break
    for i in range(len(cars)):
        if cars[i] == car:
            print(f"找到了在{i}位置")
            break
    else:
        print("找不到!")
        
