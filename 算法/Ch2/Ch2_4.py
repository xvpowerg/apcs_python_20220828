y = [x ** 2 for x in range(1,10)]
print(y)
z = [x+10 for x in range(1,10) if x%2 != 0]
print(z)
celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = [9/5*x+32 for x in celsius]
print(fahrenheit)
