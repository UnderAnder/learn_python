#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    while 1:
        if wall_is_above() == False:
            move_up()
            break
        if wall_is_beneath() == False:
            move_down()
            break
        if wall_is_on_the_left() == False:
            move_left()
            break
        if wall_is_on_the_right() == False:
            move_right()
            break


if __name__ == "__main__":
    run_tasks()
