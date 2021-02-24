#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_2_1():
    move_down(2)
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up(2)
    fill_cell()
    move_left()


if __name__ == "__main__":
    run_tasks()
