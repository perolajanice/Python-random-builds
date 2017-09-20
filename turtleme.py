import turtle

col = input("select background colour")
coll = input("select turtle colour")

wn = turtle.Screen()
wn.bgcolor(col)

perola = turtle.Turtle()
perola.color(coll)
perola.pensize(3)

janice = turtle.Turtle()
janice.color("green")
janice.pensize(1)

cruz = turtle.Turtle()
cruz.pensize(5)



for i in [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18]:
    perola.forward(200)
    perola.left(260)


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
    janice.forward(100)
    janice.left(130)

for aColor in ["red", "yellow", "pink", "white", "orange", "purple", "black"]:
    cruz.color(aColor)
    cruz.right(95)
    cruz.forward(50)


wn.exitonclick()
