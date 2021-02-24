#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    i = 0
    while True:
        while not wall_is_on_the_left():
            move_left()
            i += 1
            if not wall_is_beneath():
                move_down()
                i = 0
        if i > 20:
            break
        else:
            while True:
                while not wall_is_on_the_right():
                    move_right()
                    i += 1
                    if not wall_is_beneath():
                        move_down()
                        i = 0
                if wall_is_on_the_right():
                    break

if __name__ == "__main__":
    run_tasks()
