cars = ['Honda','Toyota','Ford','BMW']    
print("pop之前:",cars)
print("pop之前長度:",len(cars))
popCar = cars.pop()
print("pop之後:",cars)
print("pop之後長度:",len(popCar))
print("pop元素:",popCar)
print("===================")
popCar = cars.pop(1)
print("pop之後:",cars)
print("pop之後長度:",len(popCar))
print("pop元素:",popCar)