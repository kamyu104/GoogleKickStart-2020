# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem C. Combination Lock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
#
# Time:  O(WlogW)
# Space: O(W)
#

def combination_lock():
    W, N = map(int, raw_input().strip().split())
    X = map(lambda x:int(x)-1, raw_input().strip().split())

    X.sort()
    for i in xrange(len(X)-1):  # make it as circular array
        X.append(X[i]+N)
    prefix = [0]
    for x in X:
        prefix.append(prefix[-1]+x)
    return min((prefix[(i+W-1)+1]-prefix[(i+(i+W-1)+1)//2])-(prefix[(i+(i+W-1))//2+1]-prefix[i]) for i in xrange(W))  # find median of window with min number of moves

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, combination_lock())
