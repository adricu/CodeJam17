# -*- coding: utf-8 -*-
#===============================================================================
from __future__ import unicode_literals


#===============================================================================
def read_input(strip=True):
    return raw_input().strip() if strip else raw_input()


def read_input_multi(strip=True):
    return read_input(strip).split()


def read_int():
    return int(read_input())


def read_int_multi():
    return [int(s) for s in read_input_multi()]


def print_solution(i, solution):
    print('Case #{}: {}'.format(i, solution))
#===============================================================================


#------------------------------------------------------------------------------

def is_resolved(S):
    pass


def make_string(S):
    """Takes a list and concatenates all his members in a string"""
    return ''.join(S)


def time_to_d(K, S, D):
    return float(D - K) / float(S)


def solve():
    D, N = read_int_multi()
    horses_time = []

    for _ in xrange(N):
        K, S = read_int_multi()
        horses_time.append(time_to_d(K, S, D))

    slowest = max(horses_time)
    return D / slowest



#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
