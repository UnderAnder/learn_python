#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    f = 0
    d = 0
    move_down()
    while 1:
        if wall_is_above():
            move_left()
            if wall_is_on_the_left():
                break
        if f == 0 and wall_is_beneath() == False and wall_is_above() == False:
            move_down()
        if wall_is_beneath():
            move_right()
            f = 1
        if wall_is_beneath() == False and f == 1:
            move_down()
            move_left()
            f = 0


if __name__ == "__main__":
    run_tasks()
