# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
#
# Time:  O(N)
# Space: O(N)
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())

    prefix = [0]  # prefix sum of harmonic progression
    for n in xrange(1, N):
        prefix.append(prefix[-1]+1.0/n)
    # EV[i] = (1/i + ... + 1/3 + 1/2 + 1) + (1/((N-1)-i) + ... + 1/3 + 1/2 + 1)
    return sum(a*(prefix[i]+prefix[(N-1)-i]) for i, a in enumerate(A))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
