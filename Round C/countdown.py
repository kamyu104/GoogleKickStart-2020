# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round C - Problem A. Countdown
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
#
# Time:  O(N)
# Space: O(1)
#

def countdown():
    N, K = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())

    result, curr = 0, K
    for x in A:
        if x != curr:
            curr = K
        if x == curr:
            curr -= 1
            if curr == 0:
                result += 1
                curr = K
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, countdown())
