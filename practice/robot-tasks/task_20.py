#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(12):
        for j in range(28):
            if i % 2 == 0:
                if j == 27:
                    i += 1
                    move_down()
                    fill_cell()
                    continue
                move_right()
                fill_cell()
            else:
                if j == 27:
                    i += 1
                    move_down()
                    continue
                fill_cell()
                move_left()

    move_right()


if __name__ == "__main__":
    run_tasks()
