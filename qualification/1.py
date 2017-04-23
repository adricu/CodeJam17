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

def flip(S, K, i_pos):
    for j in xrange(K):
        pos_to_flip = i_pos + j
        S[pos_to_flip] = '-' if S[pos_to_flip] == '+' else '+'


def is_resolved(S):
    return '-' not in S


def make_string(S):
    return ''.join(S)


def solve():
    past_states = []
    S, K = read_input_multi()
    length = len(S)
    past_states.append(S)
    S = list(S)
    K = int(K)

    while not is_resolved(S):
        idx_to_flip = None
        best_to_flip = 0
        for idx, c in enumerate(S):
            n_nh = 0
            if c == '-' and idx + K - 1 < length:
                n_nh = 1
                for c_ in S[idx + 1:idx + K]:
                    if c_ == '-':
                        n_nh = n_nh + 1
            else:
                continue
            if n_nh == K:
                idx_to_flip = idx
                break
            elif n_nh > best_to_flip:
                best_to_flip = n_nh
                idx_to_flip = idx
        if idx_to_flip is not None:
            flip(S, K, idx_to_flip)
        if is_resolved(S):
            return len(past_states)
        string_S = make_string(S)
        if string_S in past_states:
            return 'IMPOSSIBLE'

        past_states.append(string_S)
    return 0


#===============================================================================
if __name__ == '__main__':
    test_cases = read_int()
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
