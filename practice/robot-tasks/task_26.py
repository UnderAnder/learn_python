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

@task(delay=0.02)
def task_2_4():
    i = 0
    j = 0
    while j < 5:
        move_down()
        while i < 10:
            cross()
            if i != 9:
                move_down()
                move_right(4)
            i += 1
        if j != 4:
            move_down(4)
        move_left(36)
            
        i = 0
        j += 1

if __name__ == "__main__":
    run_tasks()
