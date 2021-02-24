#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 0
    move_right()
    while not wall_is_on_the_right():
        i += 1
        fill_cell()
        for j in range(0,i):
            if wall_is_on_the_right():
                break
            move_right()
        
        


if __name__ == "__main__":
    run_tasks()
