import turtle
wn = turtle.Screen()
wn.bgcolor("pink")
perola = turtle.Turtle()
perola.color("purple")
perola.shape("turtle")

print(range(8, 200, 1))
perola.up()
for size in range(8, 200, 1):
    perola.stamp()
    perola.forward(size)
    perola.right(24)
