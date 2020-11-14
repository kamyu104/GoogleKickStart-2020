# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2020 Round D - Problem A. Record Breaker
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171
#
# Time:  O(N)
# Space: O(1)
#

def record_breaker():
    N = input()
    V = map(int, raw_input().strip().split())

    result = max_v = 0
    for i, v in enumerate(V):
        if (i == 0 or v > max_v) and (i+1 == len(V) or v > V[i+1]):
            result += 1
        max_v = max(max_v, v)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, record_breaker())
