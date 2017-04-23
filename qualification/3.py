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

def solve():
    N, K = read_input_multi()
    N = int(N)
    K = int(K)
    div = N / K
    rem = N % K
    
    if 

    maxx = div
    minn = div - rem

    return '{} {}'.format(maxx, minn)


#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
