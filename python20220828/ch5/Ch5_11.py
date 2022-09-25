import calculator as cau #取別名
import calculator
from calculator  import calcBmi,getMessage

area = calculator.calcArea(10)
print(area)
tf = cau.toFahrenheit(28)
print(tf)

bmi = calcBmi(180,72)
msg = getMessage(bmi)
print(msg)
