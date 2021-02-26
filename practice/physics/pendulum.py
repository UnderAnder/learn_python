import math

import graphics as gr


SIZE_X = 800
SIZE_Y = 800
LENGHT = 200


def draw(x, y, radius, window):
    bob = gr.Circle(gr.Point(x, y), radius)
    bob.setFill("red")
    bob.draw(window)

    return bob


def get_path(angle):
    x = SIZE_X/2 + LENGHT * math.sin(angle)
    y = 50 + LENGHT * math.cos(angle)
    return x, y


def main():
    window = gr.GraphWin("Pendulum", SIZE_X, SIZE_Y)
    angle = 120
    velocity = 0

    pendulum = draw(SIZE_X // 2, LENGHT, 15, window)

    while True:
        acceleration = -0.005 * math.sin(angle)
        velocity += acceleration
        angle += velocity

        x, y = get_path(angle)
        pendulum.move(x - pendulum.p1.x , y - pendulum.p1.y)

        gr.time.sleep(0.05)


if __name__ == "__main__":
    main()
