carList = ['Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda']
carSet  = {'Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda'}


print("車輛清單:",carList)
print("第三台車:",carList[3-1])
print(f"共有{len(carSet)}品牌")

LuxuryCar  = {"Audi", "Benz", "BMW"}
LuxuryDict = {"Audi":0, "Benz":0, "BMW":0}

for car in carList:
    if car in LuxuryCar:
        LuxuryDict[car] += 1
        
print("豪車品牌:",LuxuryDict)
