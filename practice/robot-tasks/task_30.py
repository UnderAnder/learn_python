#!/usr/bin/python3

from pyrob.api import *


def fill_triangles(size):
    for j in range(0, size+1):
        for i in range(0, size+1):
            if i != j and i != size - j:
                fill_cell()
            if i == size:
                break
            if j % 2 == 0:
                move_left()
            else:
                move_right()
        if j == size:
            break
        move_down()


@task(delay=0.05)
def task_9_3():
    size = 0
    while not wall_is_on_the_right():
        move_right()
        size += 1
    fill_triangles(size)


if __name__ == "__main__":
    run_tasks()
