# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem B. Metal Harvest
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4b8b
#
# Time:  O(NlogN)
# Space: O(1)
#

def metal_harvest():
    N, K = map(int, raw_input().strip().split())
    result = right = 0
    intervals = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    intervals.sort()
    for S, E in intervals:
        if E <= right:
            continue
        right = max(right, S)
        count = ((E-right)-1)//K+1
        right += K*count
        result += count
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, metal_harvest())
