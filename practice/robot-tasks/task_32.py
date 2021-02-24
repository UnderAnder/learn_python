#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    n = 0
    while True:
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    n += 1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        else:
            fill_cell()
        move_right()
        if not wall_is_on_the_left() and not wall_is_beneath():
            break
    mov('ax',n)

if __name__ == "__main__":
    run_tasks()
