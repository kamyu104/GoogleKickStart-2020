# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem B. Bus Routes
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
#
# Time:  O(N)
# Space: O(1)
#

def bus_routes():
    N, D = map(int, raw_input().strip().split())
    X = map(int, raw_input().strip().split())

    for x in reversed(X):
        D -= D%x
    return D

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bus_routes())
