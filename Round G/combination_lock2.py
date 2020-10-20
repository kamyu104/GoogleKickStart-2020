# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem C. Combination Lock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
#
# Time:  O(WlogW)
# Space: O(1)
#
# this solution is optimized from combination_lock.py
#

def combination_lock():
    W, N = map(int, raw_input().strip().split())
    X = map(lambda x:int(x)-1, raw_input().strip().split())

    X.sort()
    result = float("inf")
    prefix_j = sum(X[i] for i in xrange(W))
    prefix_m2_1 = sum(X[i] for i in xrange(((W-1)+1)//2))
    prefix_m1 = sum(X[i] for i in xrange(((W-1)//2)+1))
    prefix_i_1 = 0
    for i, x in enumerate(X):
        result = min(result, (prefix_j-prefix_m2_1) - (prefix_m1-prefix_i_1))
        ni, nj = i+1, (i+1)+(W-1)
        m1, m2 = (ni+nj)//2, (ni+nj+1)//2
        prefix_j += X[nj-W]+N
        prefix_m2_1 += X[(m2-1)-W]+N if m2-1 >= W else X[m2-1]
        prefix_m1 += X[m1-W]+N if m1 >= W else X[m1]
        prefix_i_1 += X[ni-1]
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, combination_lock())
