# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem B. Maximum Coins
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23
#
# Time:  O(N^2)
# Space: O(N)
#

from collections import Counter

def maximum_coins():
    N = input()
    C = [map(int, raw_input().strip().split()) for _ in xrange(N)]

    count = Counter()
    for i, row in enumerate(C):
        for j, v in enumerate(row):
            count[i-j] += v
    return max(count.itervalues())

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, maximum_coins())
