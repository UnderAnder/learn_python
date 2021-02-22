#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    move_down()
    move_right()
    n = 0
    while not wall_is_beneath():
        n += 1
        for i in range(n):
            fill_cell()
            move_right()
        for i in range(n):
            move_left()
        move_down()


if __name__ == "__main__":
    run_tasks()
