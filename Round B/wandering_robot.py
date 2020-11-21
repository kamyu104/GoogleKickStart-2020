# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round B - Problem D. Bus Routes
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
#
# Time:  O(min(W, H))
# Space: O(min(W, H))
#

from math import log, exp

def log_p(logfac, n, r):  # log(C(n, r)/2^(n+1))
    return logfac[n]-logfac[r]-logfac[n-r]-(n+1)*log(2)  # math.log is O(1) due to less precision

def wandering_robot():
    W, H, L, U, R, D = map(int, raw_input().strip().split())

    logfac = [0.0]
    for x in xrange(1, ((W+H-2)-1)+1):
        logfac.append(logfac[-1] + log(x))
    result = 0.0
    if D < H:
        for x in xrange(1, L):
            result += exp(log_p(logfac, x+D-2, x-1))  # float exp (math.exp) is O(1) due to less precision
    if R < W: 
        for y in xrange(1, U):
            result += exp(log_p(logfac, R+y-2, y-1))  # float exp (math.exp) is O(1) due to less precision
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wandering_robot())
