#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    f = 0
    while 1:
        move_right()
        if wall_is_beneath():
            f = 1
        if wall_is_beneath() == False and f == 1:
            break


if __name__ == "__main__":
    run_tasks()
