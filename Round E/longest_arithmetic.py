# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round E - Problem A. Longest Arithmetic
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed
#
# Time:  O(N)
# Space: O(1)
#

def longest_arithmetic():
    N = input()
    A = map(int, raw_input().strip().split())

    result = 1
    d, count = None, 0
    for i in xrange(N-1):
        if A[i+1]-A[i] == d:
            count += 1
            continue
        result = max(result, count)
        d = A[i+1]-A[i]
        count = 2
    return max(result, count)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, longest_arithmetic())
