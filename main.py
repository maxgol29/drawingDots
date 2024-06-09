import random
import turtle as t
import colorgram as color



colors = color.extract('image.jpg', 32)

lst_colors = []
for index in range(len(colors)):
    color = colors[index].rgb
    r, g, b = color
    lst_colors.append((r, g, b))


def random_color():
    return lst_colors[random.randint(0, 31)]


print(lst_colors)
maks = t.Turtle()
maks.speed("fastest")
t.colormode(255)
maks.penup()
maks.setheading(225)
maks.forward(300)
maks.setheading(0)


for col in range(10):
    for row in range(10):
        maks.dot(20, random.choice(lst_colors))
        maks.forward(50)
    maks.setheading(90)
    maks.forward(50)
    maks.setheading([0, 180][col % 2 == 0])
    maks.forward(50)

screen = t.Screen()
screen.exitonclick()