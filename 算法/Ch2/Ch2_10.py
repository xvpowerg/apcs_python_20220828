poly1 = [1,-3,2]#f(x) = 2𝑥^2 -3x + 1
x = 3
fx = 0
for i in range(len(poly1)):#0 1 2
    fx += poly1[i] * x ** i
print(f"f({x})={fx}")

poly2 = [3, 2, 2, -3, 1, 1, 0]
y = 4
fy = 0
for j in range(poly2[0]):
    fy += poly2[2*j+1]*y**poly2[2*(j+1)]
print('f(%d) ='%y, fy)
