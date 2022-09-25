import turtle
sean = turtle.Turtle()
sean.name = "sean"
print(sean.name)
sean.shape("turtle")
sean.pencolor('red')
sean.fillcolor('blue')
sean.pensize(2)

for i in range(1,5):
    sean.forward(100)
    sean.right(90)
