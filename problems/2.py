# -*- coding: utf-8 -*-
#===============================================================================
#from __future__ import unicode_literals

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

def is_tidy(N):
    st = str(N)
    if len(st) == 1:
        return True, None
    pre = int(st[0])

    for idx, c in enumerate(st[1:]):
        act = int(c)
        if act >= pre:
            pre = act
            continue
        return False, idx
    return True, None


def search_last_tidy(N):
    tidy, i = is_tidy(N)
    if tidy:
        return N
    a = '9' * (len(N) - i - 1)
    N_int = int(N)
    b = 10**len(a)
    N_int = ((N_int / b) * b) + int(a) - b
    return search_last_tidy(str(N_int))


def solve():
    N = read_input(strip=True)
    return search_last_tidy(N)


#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
