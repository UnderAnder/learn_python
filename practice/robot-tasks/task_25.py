#!/usr/bin/python3

from pyrob.api import *

def cross():
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

@task
def task_2_2():
    i = 0
    move_down(2)    
    while i < 5:
        cross()
        if i != 4:
            move_down()
            move_right(4)
        i += 1


if __name__ == "__main__":
    run_tasks()
