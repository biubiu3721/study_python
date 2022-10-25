import numpy as np
import sys

sys.setrecursionlimit(100000)
a_win = []
b_win = []


def forward(N, cur_sum, steps_log, delta):
    global a_win
    global b_win
    cur_sum += delta
    steps_log.append(delta)
    if cur_sum >= N:
        len_steps_log = len(steps_log)
        if len_steps_log % 2 == 0:
            print("a_win")
            a_win.append(steps_log)
        else:
            print("b_win")
            b_win.append(steps_log)
        print("len_steps", len_steps_log)
        print("shedule", steps_log)

        return
    else:
        max_len = min(len(steps_log), N - cur_sum)
        for i in range(1, max_len + 1):
            forward(N, cur_sum, steps_log.copy(), i)


cur_sum = 0
steps_log = []
cur_rounds = 0
delta = 1
N = 10
forward(N, cur_sum, steps_log, delta)

print("a_win", len(a_win), a_win)
print("a_win", len(b_win), b_win)

"""
    Cal the minimum steps to count N.
"""
def min_step(N):
    x = N - 1
    start = 1
    step = 1 # for last 1.
    while x > 0:
        x -= start
        start += 1
        step += 1
    return step
"""
The one 'will' lose control ability when cum_sum(step) == N -1.
So from next step, control ability belongs to the other one.
Start from N = 2.
"""

def print_winner(N):
    if min_step(N) % 2 == 0:
        print("*** the winner is a")
    else:
        print("*** the winner is b")

for n in range(2, 20, 1):
    print("N = ", n)
    print_winner(n)
print("2021")
print_winner(2021)