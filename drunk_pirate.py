import turtle
import random

def drunk_pirate(n):
    t = turtle.Turtle()
    r_or_l = True

    for i in range(n):
        if r_or_l == True:
            t.right(random.randint(1, 360))
        else:
            t.left(random.randint(1, 360))

        r_or_l = not r_or_l
        t.forward(100)

drunk_pirate(12)
