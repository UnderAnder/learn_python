#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while 1:
        if wall_is_above() == False and wall_is_beneath():
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == "__main__":
    run_tasks()
