import graphics as gr
import math
win = gr.GraphWin("mayatnik", 500, 500)
dt = 10
a = 0
v = 0.05
r = 20
L = 200
x = 250
y = 10+L*math.cos(a)
nit = gr.Line(gr.Point(250, 10), gr.Point(x, y))
nit.draw(win)
circle = gr.Circle(gr.Point(x, y), r)
circle.setFill("black")
circle.draw(win)


def change():
    global a, v
    a = a+v*dt/r
    v = v-0.01*math.sin(a)
    return a


def mv():
    global nit, circle, x, y, L
    a = change()
    x = L*math.sin(a)+250
    y = L*math.cos(a)+10
    nit.undraw()
    circle.undraw()
    circle.move(x, y)
    nit = gr.Line(gr.Point(250, 10), gr.Point(x, y))
    nit.draw(win)
    circle = gr.Circle(gr.Point(x, y), r)
    circle.setFill("black")
    circle.draw(win)


def main():
    for i in range(500):
        change()
        mv()
        gr.time.sleep(0.1)


main()
