#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    while 1:
        if wall_is_beneath():
            move_right()
        else:
            break


if __name__ == "__main__":
    run_tasks()
