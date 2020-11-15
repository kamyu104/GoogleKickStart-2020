# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round H - Problem C. Rugby
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027
#
# Time:  O(NlogN)
# Space: O(N)
#

def rugby():
    N = input()
    X, Y = [0]*N, [0]*N
    for i in xrange(N):
        X[i], Y[i] = map(int, raw_input().strip().split())

    X.sort()
    X = [x-i for i, x in enumerate(X)]
    X.sort()
    Y.sort()
    return  sum(abs(x-X[(N-1)//2]) for x in X) + sum(abs(y-Y[(N-1)//2]) for y in Y)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rugby())
