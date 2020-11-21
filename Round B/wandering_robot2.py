# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem D. Wandering Robot
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
#
# Time:  O(W + H)
# Space: O(W + H)
#

from math import log, exp

def prob(logfac, n, r):  # C(n, r)/2^n
    return exp(logfac[n]-logfac[r]-logfac[n-r]-n*log(2))  # math.exp / math.log is O(1) due to less precision

def wandering_robot():
    W, H, L, U, R, D = map(int, raw_input().strip().split())

    logfac = [0.0]
    for x in xrange(1, ((W+H-2)-1)+1):
        logfac.append(logfac[-1] + log(x))
    result = 0.0
    if D < H:
        for x in xrange(1, L):
            result += prob(logfac, x+D-2, x-1)/2.0
    if R < W: 
        for y in xrange(1, U):
            result += prob(logfac, R+y-2, y-1)/2.0
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wandering_robot())
