# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
#
# Time:  ctor:    O(MAX_N)
#        runtime: O(N)
# Space: ctor:    O(MAX_N)
#        runtime: O(1)
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())

    H = [1.0/n for n in xrange(1, N+1)]
    P = [0]
    for h in H:
        P.append(P[-1]+h)
    # EV[i] = (1 + 1/2 + 1/3 + ... + 1/i) + (1/((N-1)-i) + 1/((N-1)-i+1) + ... + 1/3 + 1/2 + 1
    return sum(a*(P[i]+P[(N-1)-i]) for i, a in enumerate(A))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
